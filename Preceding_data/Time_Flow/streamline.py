"""
形成 final_stream 数据流
"""
import pymongo


class StreamLine:

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


# p1的主函数
def p1_main_function():
    p1_data = StreamLine("p1", "yanglao", "temp_streamline")
    p1_data.update_time_flow_as_time()
    del p1_data  # 销毁对象


# p2的主函数
def p2_main_function():
    p2_data = StreamLine("p2", "yanglao", "temp_streamline")
    p2_data.update_time_flow_as_time()
    del p2_data  # 销毁对象


# p3的主函数
def p3_main_function():
    p3_data = StreamLine("p3", "yanglao", "temp_streamline")
    p3_data.update_time_flow_as_time()
    del p3_data  # 销毁对象


if __name__ == '__main__':
    """
    p3_main_function()
    """