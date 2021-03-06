"""
将老人的居住信息，先测试写入文本，再写入数据库！
"""
import codecs
import pymongo


class InputPersonData:

    # 全局变量
    varString = "admin你好！"
    x = "123"

    # 构造函数
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.name = 'admin'

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

    @classmethod
    def test2(cls):
        print(cls)
        print('test2')
        print(InputPersonData.x)
        print('----------------')

    @staticmethod
    # 写入MongoDB数据库
    def input_database():
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.moneyfrom
        # 添加单条记录到集合中
        money = {"_id": 3, "pPer_id": "p3", "moName": "退休金/养老金"}
        collection.insert(money)
        # 查询所有记录
        print("查询所有记录: ")
        for data in collection.find():
            print(data)
        client.close()

    @staticmethod
    # 查询所有collections
    def find_all():
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.perinfo
        # 查询所有
        for data in collection.find():
            print(data)
        print("总记录数为：", collection.find().count())
        client.close()

    @staticmethod
    def update_database():
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.perinfo
        collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        client.close()

    @staticmethod
    def find_one():
        # 查找单个数据
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.perinfo
        for u in collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
        client.close()

    @staticmethod
    def delete_one():
        # 删除指定的一条记录
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.perinfo
        for u in collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
        collection.remove({"_id": 1})
        client.close()

    @staticmethod
    def delete_all():
        # 删除指定的一条记录
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.perinfo
        collection.remove()
        client.close()


# 它打开一个文件，在该文件中的内容写入内容，但文件没有写入权限，发生了异常：
def writefile():
    text = {"_id": 1, "pPer_id": "p1"}
    try:
        fh = codecs.open("testfile", "w+", 'utf-8')
        print("字典str: ", text)
        fh.write(text.__str__())
    except IOError:
        print("Error : 没有找到文件或者读取文件失败！")
    else:
        print("内容写入文件成功！")
        fh.close()


if __name__ == '__main__':
    in1 = InputPersonData()
    # in1.writefile()
    # InputPersonData.writefile()  # 作用同上
    InputPersonData.input_database()
    # in1.update_database()
    # in1.find_one()
    # in1.delete_one()
    # in1.delete_all()
    # in1.find_all()
