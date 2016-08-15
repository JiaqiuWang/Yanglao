"""
根据trans数据库中的数据，形成最终的transaction
"""

import datetime
import pymongo
import time


class Transaction:

    # 类公有变量
    client = pymongo.MongoClient("192.168.1.228", 27017)
    # 或者127.0.0.1
    count = 0
    # 用于排序的队列
    list_sort = []
    # 每个人streamline 的计数
    psl_count = 1
    # trans_no : fp_tarns表格的计数字段
    trans_no = 0
    # 计数的变量，用于比较记录总数和已经插入数据库的数目
    count_already_inserted = 0

    # 构造函数
    def __init__(self, user_id, db_name, collection_name, transaction, span, store_col_name):
        self.user_id = user_id
        self.db_name = db_name
        self.collection_name = collection_name
        self.new_transaction = transaction
        self.span = span
        self.store_col_name = store_col_name
        self.drop_collection(store_col_name)

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        self.client.close()
        print(class_name, "销毁")

        # 返回日期，不包括时间

    @classmethod
    def get_date_from_times(cls, times):
        try:
            date_var = time.strptime(times, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
        else:
            # print("error_date_var:", date_var.tm_hour)
            date_result = datetime.datetime(date_var[0], date_var[1], date_var[2],
                                            date_var[3], date_var[4], date_var[5])
            return date_result

    # 查询所有trans 集合的方法
    def find_all_trans(self):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        var_cursor = collection.find({"pPer_id": self.user_id})  # 查找一个人的所有记录
        count = var_cursor.count()  # 计算记录的数量
        start_date = None
        first_date = ""
        second_date = ""
        for var_document in var_cursor:
            self.count_already_inserted += 1
            str_times = var_document.get("times")
            _id = var_document.get("_id")
            print("_id:", _id, "str_times:", str_times, "type-str_time:", type(str_times))
            if self.count_already_inserted == count:
                print("最后一个事务：", self.list_sort)
                self.trans_no += 1
                self.insert_transaction(self.list_sort, self.trans_no)
                break
            if start_date is None:
                # 获取第一天document的日期(不包括时间)
                temp_date = self.get_date_from_times(str_times)
                if temp_date is None:  # 如果该记录只包含日期，没有时间的话，把他直接加入该事务中
                    self.list_sort.append(var_document)
                    print("count:", self.count_already_inserted, " _id", _id, "is add to list!")
                    continue
                else:   # 都包含日期和时间
                    first_date = temp_date
                    self.list_sort.append(var_document)
                    print("count:", self.count_already_inserted, " _id", _id, "is add to list!")
                    start_date = first_date
                    # print("first_date:", first_date)
            else:
                temp_date = self.get_date_from_times(var_document.get("times"))
                if temp_date is None:  # 如果该记录只包含日期，没有时间的话，把他直接加入该事务中
                    self.list_sort.append(var_document)
                    print("count:", self.count_already_inserted, " _id", _id, "is add to list!")
                    continue
                else:
                    if first_date != "":
                        second_date = temp_date
                    else:
                        print("first_date is null! ")
                    # 计算 second_date - first_date
                    minus_value = self.second_date_minus_first_date(second_date, first_date)
                    if minus_value <= self.span:
                        self.list_sort.append(var_document)
                        print("count:", self.count_already_inserted, " _id", _id, "is add to list!")
                        if self.count_already_inserted == count:
                            print("最后一个事务：", self.list_sort)
                            self.trans_no += 1
                            self.insert_transaction(self.list_sort, self.trans_no)
                    else:
                        print("相邻的服务大于时间间隔阈值span:", minus_value, "输出list:", self.list_sort)
                        self.trans_no += 1
                        self.insert_transaction(self.list_sort, self.trans_no)
                        self.list_sort = []
                        self.list_sort.append(var_document)
                        print("count:", self.count_already_inserted, " _id", _id, "is add to list!")
                        first_date = second_date
        print("count: ", count, " tran_no:", self.trans_no, " count_already_insert:", self.count_already_inserted)

    # 计算日期相减
    @staticmethod
    def second_date_minus_first_date(second_date, first_date):
        print("second_date:", second_date, "first_date:", first_date)
        result = second_date - first_date
        return result.seconds

    # 插入到事务transaction数据库中
    def insert_transaction(self, list_trans_one, trans_no):
        print("type-list_trans_one:", type(list_trans_one))
        for item in list_trans_one:
            print("type-item:", type(item), "i:", item)
            # 加入trans_no字段，向每个字典类型的item中
            item.setdefault("trans_no", trans_no)
            # 插入元操作
            self.insert_basic_database(self.db_name, self.store_col_name, item)

    # 插入数据库元操作
    def insert_basic_database(self, db_name, collection_name, item):
        db = self.client.get_database(db_name)
        collection = db.get_collection(collection_name)
        # 添加单条记录到集合中
        collection.insert(item)

    # 删除数据collection，慎重使用：
    def drop_collection(self, drop_collection):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(drop_collection)
        collection.drop()  # 删除全部collection

    @staticmethod
    def cal_time():
        date1 = "2015-10-03 13:52:35"
        date2 = "2015-10-03 13:56:45"
        date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
        d1 = date1.timestamp()
        d2 = date2.timestamp()
        print("date2:", date2, "d2:", d2, "type:", type(d2),
              "\ndate1:", date1, " d1:", d1, "type:", type(d1))
        result = date2 - date1
        print("date2 - date1: ", result.seconds, "seconds. Type-result: ", type(result.seconds))
        return date2 - date1


def operating_main():
    uid = "p3"  # 参数uid
    db = "yanglao"  # 数据库名称
    read_collection_name = "trans"  # 需要读取的数据库名称
    new_transaction = "transaction"  # 需要新生成的数据库名称，即最后的事务数据
    span = 6000   # 时间间隔参数，单位为秒
    # 先删除所有数据: fp-trans，然后重新插入，类似内存一样
    store_col_name = "fp_trans_"+uid
    trs = Transaction(uid, db, read_collection_name, new_transaction, span, store_col_name)
    # 查询trans 集合中的数据
    trs.find_all_trans()


if __name__ == '__main__':
    start_time = time.clock()
    operating_main()
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间
