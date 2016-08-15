"""

"""
import pymongo
import random
import datetime


class AddService:

    # 构造函数
    def __init__(self, db_name, collection_name, service_name):
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient("127.0.0.1", 27017)
        # 获取数据库
        self.db = self.client.get_database(db_name)
        # 获取集合
        self.collection = self.db.get_collection(collection_name)
        self.service_name = service_name

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
        self.client.close()

    # 添加服务名称
    def add_service_name(self):
        self.collection.update_many({}, {"$set": {"service_name": self.service_name}})
        # self.collection.update({}, {"$set": {"service_name": "体检服务"}}, false, ture)
        # data.setdefault("service_name", "体检服务")


if __name__ == '__main__':
    var_as = AddService("yanglao", "specialtreat", "治疗服务")
    var_as.add_service_name()

