"""
形成temp_streamline数据流
"""
import pymongo
import re


class TimeFlow:

    # 类公有变量
    client = pymongo.MongoClient("127.0.0.1", 27017)
    count = 0

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

    # 类中函数-获取所有collections
    def get_all_collections_name(self):
        # 获取数据库
        db = self.client.get_database(self.db_name)
        # 获取集合
        collection = db.collection_names()
        return collection

    # 类中函数-循环获取每个collection的名称
    def get_each_collection(self, list_cols):
        for var_list_cols in list_cols:
            print("list_cols: ", var_list_cols)
            # 获取每一个collection的记录，并按照时间线从前往后的顺序排列
            if var_list_cols is not self.db_name:
                self.get_each_col_all_records(var_list_cols)

    # 获取每一个collection的记录，并按照时间线从前往后的顺序排列
    def get_each_col_all_records(self, var_list_cols):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(var_list_cols)
        cursor_col = collection.find_one({"pPer_id": self.user_id})
        if cursor_col is not None:
            for data in collection.find_one():
                print("type-data: ", type(data), ", data: ", data)
                # 正则表达式匹配，找到关于时间或者日期的字段，并按照日期从小到大的排序
                date_time = self.get_date_time(data)
                if date_time is None:
                    continue
                print("date_time: ", date_time)
                self.sort_time_flow(date_time, collection)
            # for key in data.keys():
            #    print("key: ", key)

    # 输入每个collection的关于时间日期的字段名，然后按照时间从小到大排序
    def sort_time_flow(self, date_time, collection):
        # for data in collection.find({"pPer_id": self.user_id}, {"_id": 0}).sort(date_time, 1).limit(10):
        for data in collection.find({"pPer_id": self.user_id}, {"_id": 0}).sort(date_time, 1):
            self.count = self.get_var_id()
            data.setdefault("_id", self.count)
            print("type_data: ", type(data), "data_id: ", data.get("_id"), "count: ", self.count, "data: ", data)
            data.setdefault("_id", self.count)
            # 将每一条数据新写入到时间流数据之中
            self.insert_database_time_flow(data)
            self.count += 1

    # 插入数据流数据库
    def insert_database_time_flow(self, data):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        collection.insert(data)

    # 获取temp_streamline的新的_id的数值，用于新插入数据库
    def get_var_id(self):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        cursor_count = collection.find().count()
        cursor_count += 1
        return cursor_count

    # 将streamline collection中的documents按照时间顺序重新排列
    def update_time_flow_as_time(self):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        for data in collection.find({"pPer_id": self.user_id}, {"_id": 0}).sort("times", 1):
            print("data: ", data)

    # 正则表达式匹配，找到关于时间或者日期的字段
    @staticmethod
    def get_date_time(key_str):
        match_obj_date = re.match('(.*)_date|(.*)_time', key_str, re.M | re.I)
        if match_obj_date:
            # print("matchObj.group() : ", match_obj_date.group())
            return match_obj_date.group()


# p1的主函数
def p3_main_function():
    p3_data = TimeFlow("p3", "yanglao", "temp_streamline")
    list_cols = p3_data.get_all_collections_name()
    if list_cols is not []:
        p3_data.get_each_collection(list_cols)
        # p1_data.update_time_flow_as_time()
    else:
        print("all_collections is empty!")
    del p3_data  # 销毁对象


if __name__ == '__main__':
    p3_main_function()
