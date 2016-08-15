"""

"""
import pymongo


class AddIdentity:

    # 构造函数
    def __init__(self, db_name, collection_name, pPer_id, start_index, end_index):
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient("127.0.0.1", 27017)
        # 获取数据库
        self.db = self.client.get_database(db_name)
        # 获取集合
        self.collection = self.db.get_collection(collection_name)
        self.pPer_id = pPer_id
        self.start_index = start_index
        self.end_index = end_index

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
        self.client.close()

    # 添加用户ID，pPer_id
    def add_user_id(self):
        for var in range(self.start_index, self.end_index):
            self.collection.update_one({"_id": var}, {"$set": {"pPer_id": self.pPer_id}})
        # self.collection.update({}, {"$set": {"service_name": "体检服务"}}, false, ture)
        # data.setdefault("service_name", "体检服务")


if __name__ == '__main__':
    var_as = AddIdentity("yanglao", "specialtreat", "p3", 2001, 3001)
    var_as.add_user_id()

