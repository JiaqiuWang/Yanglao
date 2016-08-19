"""
Name: PrefixSpan: 改进的——前缀投影序列模式增长算法
Author: Jia_qiu Wang(王佳秋)
Data: July, 2016
function:
"""

import time
import pymongo
import FrequentSequences


class PrefixSpanSD:
    """类公有变量"""
    client = pymongo.MongoClient("127.0.0.1", 27017)  # ip或者127.0.0.1
    db = client.get_database("yanglao")
    # 其他类公有变量
    list_dup_service = []  # 判断是否是重复service_Name
    fp_list = []  # 用于存放所有频繁序列的队列
    fp_candidate = []  # 用于判断每一次划分数据库后是否能够产生新的频繁序列模式， 划分完档次数据库后清空clear()
    # 相对支持度
    relative_sup = 0
    # 最后的一条记录的事务id (trans_no)
    final_trans_no = 0
    # 每个人的全部记录数量
    total_counts = 0
    # 将前缀序列和对应的投影索引列表，存放字典中
    dict_prefix_index = {}

    """构造函数"""
    def __init__(self, min_sup, uid, db_name, collection_read, project_records):

        self.min_sup = min_sup
        self.uid = uid
        self.db_name = db_name
        self.collection_read = collection_read
        self.project_records = project_records

    """析构函数"""
    def __del__(self):
        class_name = self.__class__.__name__
        self.client.close()
        print(class_name, "has Destroyed！")

# --------------------------------------------------------------------------------------------------------- #

    """第一部分：读取序列数据库，得到频繁一序列"""
    def findall_sequences(self, col_name):
        try:
            collection = self.db.get_collection(col_name)
            # var_cursor = collection.find({"pPer_id": self.uid}).limit(100)  # 查找一个人的所有记录
            var_cursor = collection.find({"pPer_id": self.uid})  # 查找一个人的所有记录
            count_orig_seq = var_cursor.count()  # 获取全部文档(documents)的行数
            self.total_counts = count_orig_seq
            temp_var_cursor = var_cursor.clone()  # 复制游标
            temp_find_fp_cursor = var_cursor.clone()  # 复制游标
            var_document_final = temp_var_cursor.skip(count_orig_seq-1)
            for var_doc in var_document_final:
                self.final_trans_no = var_doc.get("trans_no")   # 获取到最大的事务数
            print("final_trans_no:", self.final_trans_no)
            for var_document in var_cursor:
                # 将具有相同trans_no序列号的记录，变成一条item_sets
                print("_id:", var_document.get("_id"))
                item = var_document.get("service_name")  # 类的名称
                if item in self.list_dup_service:
                    continue                        # 重复的一项序列不需要重复计数
                else:
                    self.list_dup_service.append(item)
                temp_find_fp_cursor.rewind()
                self.find_frequent_item(item, temp_find_fp_cursor)
        except (ValueError, IOError):
            print("Exception! 终止程序，目前只扫描了一次频繁一序列 ")
        else:
            # 输出最后的所有频繁序列模式
            # self.printout_fp_list()
            # 第一部分结束，开始调用第二部分函数
            self.decide_continue_termination(var_cursor)
            # print("count_orig_seq:", count_orig_seq)

    """查找不同序列的支持度
    temp_sequence: 扫描前的一序列(字符串)，temp_var_cursor: 游标重新回到开始原点的所有文档集合
    """
    def find_frequent_item(self, temp_sequence, temp_var_cursor):
        sup_item = 0  # 序列初始支持度
        list_fp = [temp_sequence]  # 初始序列
        sp = FrequentSequences.SequencesFP(list_fp, sup_item)
        # sp = FrequentPatterns.SequencePattern(temp_sequence, sup_item)  # 为这个序列创建序列模式对象(他是候选的)
        # 查找频繁一项集 one item_set
        count_var_d = 0
        next_find_trans_no = 1  # 下一个开始查找的序列id
        current_seq = 1  # 记录当前扫描的序列id
        for var_document in temp_var_cursor:
            count_var_d += 1  # 行统计
            trans_no = var_document.get("trans_no")  # trans_no 总是从1开始
            if current_seq < trans_no:
                next_find_trans_no = trans_no
                current_seq = next_find_trans_no
            if (next_find_trans_no == trans_no) and (var_document.get("service_name") == temp_sequence):
                sp.support += 1
                next_find_trans_no = trans_no + 1
                # print("存在item的trans_no:", trans_no)
        temp_double_sop = sp.support / self.final_trans_no
        # 保留小数点后3位数 round(double, n)
        sp.support = round(temp_double_sop, 3)
        print("序列：", sp.sequence, "的支持度：", sp.support)
        if sp.support >= self.min_sup:
            self.fp_candidate.append(sp)  # 用于判断当次扫描是否产生新的频繁序列模式，扫描下一次前清空
            self.fp_list.append(sp)  # 存储所有扫描次数的频繁序列模式
            # print("type-fplist:", type(self.fp_list), "fp_list:", self.fp_list)

    """
    用于判断是否上一次扫描的局部投影数据库是否产生新的频繁序列模式
    """
    def decide_continue_termination(self, var_cursor):
        while self.fp_candidate is not None:
            print("fp_candidate is not None!")
            fp_candidate_duplicate = self.fp_candidate.copy()  # 复制上一步新生成的频繁序列模式
            self.fp_candidate.clear()   # 先清空，再看是否后续扫描具有新添加的频繁序列模式
            self.find_prefix_subset(fp_candidate_duplicate, var_cursor)
            fp_candidate_duplicate.clear()  # 等找完新的一轮频繁序列模式后，再清空复制的副本
        print("算法终止！")

# --------------------------------------------------------------------------------------------------------- #

    """第二部分：划分并且挖掘每个频繁序列的前缀子集，并且形成投影数据库，然后挖掘局部频繁项"""
    def find_prefix_subset(self, fp_candidate_duplicate, cursor_project):
        # 循环得到每个频繁的序列
        if fp_candidate_duplicate is not None:
            print("频繁的序列模式-：")
            for i in fp_candidate_duplicate:
                print("sequence: ", i.sequence, ", sup:", i.support, ", type(i):", type(i))
                # 形成前缀数据库，# 两种选择，如果数据量大于阈值，放到实际的数据库里面形成物理存储；+
                # 如果数据量小于阈值，则放入内存里面
                if self.total_counts <= self.project_records:
                    self.create_prefix_subsets_virtual_project(i.sequence, cursor_project, i.support)
                else:
                    self.create_prefix_subsets_physical_project(i.sequence, i.support, cursor_project)
                # 对所形成的投影数据库扫描一次，得出一个局部频繁项
        else:
            print("频繁序列对象为None!")

    """形成前缀数据库，虚拟投影方法"""
    def create_prefix_subsets_virtual_project(self, sequence, cursor_project, support):
        if cursor_project is None:
            print("cursor_project is None! Return!")
            return
        list_project = []
        if len(sequence) == 1:
            list_project = self.get_prefix_project_index_when_len_sequence_is_one(cursor_project, sequence)
        elif len(sequence) > 1:
            list_project = self.get_prefix_project_index_when_len_sequence_more(cursor_project, sequence)
        if list_project is None:
            print("没有获取到投影的索引序列(list_project = None)")
        else:
            print("需要形成投影的前缀(sequence)：", sequence)
            print("产生的伪投影索引队列(list_project):", list_project)
            # 将前缀序列和对应的投影索引列表，存放字典中
            self.dict_prefix_index.setdefault(tuple(sequence), list_project)
            # 第二小部分：对投影数据扫描一次，找到他的局部频繁项
            dup_cursor = cursor_project.clone()
            self.scan_fplist_for_sequences(sequence, list_project, dup_cursor, support)

    """获取前缀索引的队列  返回值是 前缀索引队列"""
    def get_prefix_project_index_when_len_sequence_more(self, cursor_project, sequence):
        # 第一种情况，放到内存里面，形成虚拟投影
        # 第一步：获取到前一个序列中的索引序列，存储后缀索引的字典数据结构为：key: (支付服务，慰藉服务)tuple，value:[10,2]list
        print("dict_prefix_index:", self.dict_prefix_index)
        # 做一个slice切片，切片范围是从队列第一个元素一直到队列倒数第一个元素(不包括倒数第一个)
        my_slice = slice(0, -1)
        pre_sequence = sequence[my_slice]
        # print("pre_sequence:", pre_sequence)
        if tuple(pre_sequence) in self.dict_prefix_index:
            print("频繁模式：", tuple(pre_sequence), "对应的待查找的后缀索引为：",
                  self.dict_prefix_index[tuple(pre_sequence)])
        # 第二部：查找该序列模式新的后缀索引，这里只处理一个序列模式的查找。 sequence：['支付服务', '慰藉服务']
        list_project = self.get_postfix_project_index_when_len_sequence_more(cursor_project, sequence,
                                                                             self.dict_prefix_index[tuple(pre_sequence)])
        print("频繁模式：", tuple(sequence), ", 对应的后缀开始索引列表：", list_project)
        return list_project

    """获取前缀索引的队列  返回值是 前缀索引队列 sequence：['支付服务', '慰藉服务']
    before_post_list: 支付服务的后缀List
    """
    def get_postfix_project_index_when_len_sequence_more(self, cursor_project, sequence, before_postfix_list):
        cursor_project.rewind()
        count_of_cursor_project = cursor_project.count()
        # 第一步：取出sequence序列中最后一个元素
        str_last_ele = sequence[-1]
        # 定义存放suffix的队列
        suffix_index = []
        # 第二部：查询每个before_postfix_list中index对应trans_no有无str_last_ele
        for var_start_index in before_postfix_list:
            single_doc = cursor_project.__getitem__(var_start_index - 1)  # 获取开始索引对应的document
            current_trans_no = single_doc.get("trans_no")  # 获取对应的trans_no
            # 获取开始索引对应的序列集合, _id生序排列
            collection = self.db.get_collection(self.collection_read)
            var_cursor = collection.find({"trans_no": current_trans_no, "service_name": str_last_ele})
            count_var_cursor = var_cursor.count()
            if count_var_cursor == 0:
                continue
            # else:
                # print("存在", count_var_cursor, "条doc, _id:", var_cursor.__getitem__(0).get("_id"))
            part_doc = var_cursor.__getitem__(0)  # 获取第一个doc
            exist_id = part_doc.get("_id")
            if exist_id == count_of_cursor_project:
                break
            # 获取下一个_id对应的trans_no, +1 对应下一个， -1对应 _getitem()从0开始获取第一个document
            trans_no_of_next_id = cursor_project.__getitem__(exist_id + 1 - 1).get("trans_no")  # 获取下一个_id对应的trans_no
            if trans_no_of_next_id == current_trans_no:
                # 可以投影得到后缀序列
                # print("exist_id:", exist_id)
                new_start_index = exist_id + 1
                suffix_index.append(new_start_index)
                # 第二小部分：对投影数据扫描一次，找到他的局部频繁项
                fp_cursor = collection.find({"trans_no": current_trans_no,  "_id": {"$gt": new_start_index}})
                for
            else:
                continue
        return suffix_index







    """获取前缀索引的队列  返回值是 前缀索引队列"""
    def get_prefix_project_index_when_len_sequence_is_one(self, cursor_project, sequence):
        # 第一种情况，放到内存里面，形成虚拟投影
        # print("虚拟投影方法！将start_id, end_id保存到dict中，然后用List保存每个dict")
        count_cp = cursor_project.count()  # 所有documents的数量
        cursor_project.rewind()
        str_sequence = sequence[-1]  # 获取序列中的最后一个service_name
        list_project = []  # 用于存放投影序列开始索引位置的队列，为每一个前缀service_name
        next_trans_no = 1
        for var_doc in cursor_project:
            # 获取数值
            temp_ser_name = var_doc.get("service_name")
            current_trans_no = var_doc.get("trans_no")
            current_id = var_doc.get("_id")
            dup_cursor = cursor_project.clone()  # 复制游标
            # 查找每个doc里面的有无前缀
            if current_trans_no == next_trans_no:
                if str_sequence == temp_ser_name:
                    # 如果找到一个前缀，那么判断下一个_id的trans_no是不是在一个trans_no里面
                    if current_id == count_cp:  # 如果是最后一个doc，剪枝不用找了
                        break
                    flag_next_trans_no = self.db_getitem(current_id, dup_cursor)
                    # print("Same: flag_next_trans:", flag_next_trans_no, ",current_tran:", current_trans_no,
                    #       ", _id:", current_id)
                    if flag_next_trans_no != current_trans_no:
                        next_trans_no = current_trans_no + 1
                        continue
                    else:
                        start_id = current_id + 1
                        list_project.append(start_id)
                        next_trans_no = current_trans_no + 1
                        continue
            elif current_trans_no > next_trans_no:
                if str_sequence == temp_ser_name:
                    # 如果找到一个前缀，那么判断下一个_id的trans_no是不是在一个trans_no里面
                    flag_next_trans_no = self.db_getitem(current_id, dup_cursor)
                    # print("Same: flag_next_trans:", flag_next_trans_no, ",current_tran:", current_trans_no,
                    #      ", _id:", current_id)
                    if flag_next_trans_no != current_trans_no:
                        next_trans_no = current_trans_no + 1
                        continue
                    else:
                        start_id = var_doc.get("_id") + 1
                        list_project.append(start_id)
                        next_trans_no = current_trans_no + 1
                        continue
                next_trans_no += 1
        return list_project

#-----------------------------------------------------------------------------------------------------------------#

    """形成前缀数据库，物理数据库投影方法"""
    @classmethod
    def create_prefix_subsets_physical_project(cls, sequence, support, cursor_project):
        # 两种选择，如果数据量大于阈值，放到实际的数据库里面形成物理存储；如果数据量小于阈值，则放入内存里面
        # 第二种情况，放到物理数据库里面
        print("物理数据库投影方法，")
        print(sequence, support, cursor_project)

#-----------------------------------------------------------------------------------------------------------------#

    # 第二小部分：对投影数据扫描一次，找到他的局部频繁项。sequence：前面的频繁序列，list_project所投影的数据库，
    # dup_cursor: 之前查询的所有游标集合， sequence: ['支付服务']
    def scan_fplist_for_sequences(self, sequence, list_project, dup_cursor, support):
        if dup_cursor is None or sequence is None or list_project is None:
            print("dup_cursor is None: ", dup_cursor)
            return
        length_list_pro = len(list_project)
        part_fplist = {}  # 局部频繁序列_字典数据结构
        for var_start_index in list_project:   # type(var_i): int  也是_id
            self.scan_fplist(dup_cursor, var_start_index, part_fplist)   # 扫一个开始id
        # 计算相对支持度
        for var_dict in part_fplist.keys():
            # print("{key:", var_dict, ", value:", part_fplist[var_dict], "}")
            list_fp = sequence.copy()  # 之前的频繁序列，队列复制，不要用赋值
            num_var = part_fplist[var_dict] / length_list_pro
            part_fplist[var_dict] = round(num_var, 3)
            # 如果局部一项的相对支持度大于等于min_sup，把他链接到前一个频繁序列模式上
            if part_fplist[var_dict] >= self.min_sup:
                list_fp.extend([var_dict])
                # print("list_fplist:", list_fp)
                fs_var = FrequentSequences.SequencesFP(list_fp, min(support, part_fplist[var_dict]))
                self.fp_list.append(fs_var)  # 全局频繁序列模式
                self.fp_candidate.append(fs_var)  # 用于判定下一次是否有候选的频繁序列模式
                print("频繁序列模式：", fs_var.sequence, ", support:", fs_var.support)
        print("输出所有的局部扫描项字典：", part_fplist)

# --------------------------------------------------------------------------------------------------------- #

    """获取局部频繁项：递归调用的函数"""
    def scan_fplist(self, dup_cursor, var_start_index, list_part_fp):
        single_doc = dup_cursor.__getitem__(var_start_index - 1)   # 获取开始索引对应的document
        current_trans_no = single_doc.get("trans_no")   # 获取对应的trans_no
        # 查询得到投影序列
        collection = self.db.get_collection(self.collection_read)
        var_cursor = collection.find({"trans_no": current_trans_no,
                                      "_id": {"$gte": var_start_index}})
        temp_list_dis_dup = []  # 用于判断一个tran_no忠是否有重复的service_name,重复的去掉
        for var_doc in var_cursor:
            service_name = var_doc.get("service_name")
            if service_name is None:
                print("service_name 获取失败！，break")
                break
            else:
                if service_name in temp_list_dis_dup:
                    continue
                else:
                    temp_list_dis_dup.append(service_name)
                    if service_name not in list_part_fp:
                        list_part_fp[service_name] = 1
                    else:
                        list_part_fp[service_name] += 1

    """输出频繁序列和对应的支持度"""
    def printout_fp_list(self):
        if self.fp_list is not None:
            print("频繁的序列模式：")
            for i in self.fp_list:
                print("sequence: ", i.sequence, ", sup:", i.support, ", type(i):", type(i))
        else:
            print("频繁序列对象为None!")

    """获取单个document的方法"""
    @classmethod
    def db_getitem(cls, _id, dup_cursor):
        flag_trans_no = dup_cursor.__getitem__(_id).get("trans_no")
        # print("flag_next_id:", dup_cursor.__getitem__(_id).get("_id"))
        if flag_trans_no is None:
            print("flag_trans_no is None!", flag_trans_no)
            return None
        else:
            return flag_trans_no


def main_operation():
    """Part1: 设置参数"""
    min_sup = 0.15  # 最小支持度阈值
    uid = "p1"  # 用户标识
    db_name = "yanglao"  # 数据库名称
    collection_read = "fp_trans_"+uid  # 待第一次扫描的序列数据库
    # 滑动时间窗口参数
    # time_windows = 0
    # 判断投影到内存或者物理数据库里面的数据量阈值
    project_records = 300000
    """Part2: 第一次扫描数据库，获取频繁1项集"""
    psp = PrefixSpanSD(min_sup, uid, db_name, collection_read, project_records)
    psp.findall_sequences(collection_read)


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行开始时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间
