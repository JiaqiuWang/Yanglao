"""
查看 final_streamline 数据流， 按照时间先后顺序排列数据
"""
import pymongo
import time
import datetime


class FindStreamLine:

    # 类公有变量
    client = pymongo.MongoClient("192.168.1.228", 27017)
    # 或者127.0.0.1
    count = 0
    # 用于排序的队列
    list_sort = []
    # 每个人streamline 的计数
    psl_count = 1

    # 构造函数
    def __init__(self, user_id, db_name, collection_name):
        self.user_id = user_id
        self.db_name = db_name
        self.collection_name = collection_name

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
        self.client.close()

    # 将streamline collection中的documents按照时间顺序重新排列
    def update_time_flow_as_time(self):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        self.count = self.get_var_id("streamline")
        psl_count = 1
        for data in collection.find({"pPer_id": self.user_id}, {"_id": 0}).sort("times", 1):
            data.setdefault("_id", self.count)
            psl_id = str(self.user_id)+"_"+str(psl_count)
            data.setdefault("psl_id", psl_id)
            self.count += 1
            psl_count += 1
            print("data: ", data)
            # 插入streamline collection中
            self.insert_sc(data)

    # 获取temp_streamline的新的_id的数值，用于新插入数据库
    def get_var_id(self, new_collection_name):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(new_collection_name)
        cursor_count = collection.find().count()
        cursor_count += 1
        return cursor_count

    # 插入streamline collection中
    def insert_sc(self, data):
        try:
            db = self.client.get_database(self.db_name)
            collection = db.get_collection("streamline")
            collection.insert(data)
        except [ConnectionError, ConnectionRefusedError]:
            print("Error")

    # 查看streamline数据集合中的所有documents
    def find_all_streamline(self):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection("streamline")
        var_cursor = collection.find({"pPer_id": self.user_id}, {"_id": 0, "psl_id": 0})
        count = var_cursor.count()
        start_date = None
        for var_document in var_cursor:
            str_times = var_document.get("times")
            print("str_times:", str_times)
            if start_date is None:
                start_date = str_times
                # 获取第一天document的日期(不包括时间)
                first_date = self.get_date_from_times(start_date)
                if first_date is None:
                    self.insert_new_sort_db(var_document)
                    continue
                self.list_sort.append(var_document)
                start_date = first_date
                print("first_date:", first_date)
            else:
                second_date = self.get_date_from_times(var_document.get("times"))
                print("second_date:", second_date)
                if start_date == second_date:
                    self.list_sort.append(var_document)
                    start_date = second_date
                else:
                    print("两天不一样，输出list:", self.list_sort)
                    # 插入到数据库中
                    self.insert_sort_list(self.list_sort)
                    self.list_sort = []
                    self.list_sort.append(var_document)
                    start_date = second_date
        print("count: ", count)
        print("list_sort:", self.list_sort)

    # 排序 队列
    def insert_sort_list(self, list_sort):
        if list_sort is []:
            print("list is empty! ")
        else:
            length = len(list_sort)
            print("type-list_sort:", type(list_sort))
            for i in range(1, length):
                value = list_sort[i]
                v_times = list_sort[i]["times"]
                # print("v_times:", v_times)
                j = i - 1
                while j >= 0 and (self.whether_less_than(list_sort[j]["times"], v_times)):
                    list_sort[j + 1] = list_sort[j]
                    j -= 1
                list_sort[j + 1] = value
            print("L:", list_sort.reverse())
            for i in list_sort:
                # 队列中的每个元素插入到数据库
                self.insert_new_sort_db(i)
                print("类型:", type(i), "队列中的每个元素:", i)
                # print("times:", i["times"])

    # 插入到新的数据里面
    def insert_new_sort_db(self, dict_i):
        db = self.client.get_database("yanglao")
        collection = db.get_collection("trans")
        # 获取trans的_id 数值
        count_trans = self.get_var_id("trans")
        dict_i.setdefault("_id", count_trans)
        psl_id = str(self.user_id) + "_" + str(self.psl_count)
        dict_i.setdefault("psl_id", psl_id)
        collection.insert(dict_i)
        self.psl_count += 1

    # 判断list_sort[j] < value, 是返回true, 否则返回false
    @staticmethod
    def whether_less_than(list_sort_j_times, v_times):
        date1 = time.strptime(list_sort_j_times, "%Y-%m-%d %H:%M:%S")
        date2 = time.strptime(v_times, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
        d1 = date1.timestamp()
        d2 = date2.timestamp()
        result = d1 - d2
        if result < 0:
            return True
        else:
            return False

    # 返回日期，不包括时间
    @classmethod
    def get_date_from_times(cls, times):
        try:
            date_var = time.strptime(times, "%Y-%m-%d %H:%M:%S")
        except:
                return None
        else:
            print("error_date_var:", date_var.tm_hour)
            date_result = datetime.datetime(date_var[0], date_var[1], date_var[2])
            return date_result

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

    @staticmethod
    def find_all_documents(person):
        start_time = time.clock()
        fsl1 = FindStreamLine(person, "yanglao", "streamline")
        fsl1.find_all_streamline()
        end_time = time.clock()
        print("Running time: %s Seconds" % (end_time - start_time))

    @staticmethod
    def insert_sort():
        list_row = [12, 5, 13, 8]
        length = len(list_row)
        print("length:", length)
        if length == 0 or length == 1:
            return list_row
        for i in range(1, length):
            value = list_row[i]
            j = i - 1
            print(i, ",value(L[i]):", value, ", j:", j)
            while j >= 0 and list_row[j] < value:
                list_row[j + 1] = list_row[j]
                j -= 1
                list_row[j + 1] = value
        # L.reverse()
        print("L:", list_row)
        return list_row


if __name__ == '__main__':
    # FindStreamLine.cal_time()
    FindStreamLine.find_all_documents("p3")
    # FindStreamLine.insert_sort()
