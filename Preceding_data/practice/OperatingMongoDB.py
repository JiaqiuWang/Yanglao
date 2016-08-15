"""
将老人基本信息，先测试写入文本，再写入数据库！
"""
import codecs
import pymongo
import datetime


class InputPersonData:

    # 全局变量
    varString = "admin你好！"

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
    # 它打开一个文件，在该文件中的内容写入内容，但文件没有写入权限，发生了异常：
    def writefile():
        str = {}
        try:
            fh = codecs.open("testfile", "w+", 'utf-8')
            print("字典str: ", str)
            fh.write(str.__str__())
        except IOError:
            print("Error : 没有找到文件或者读取文件失败！")
        else:
            print("内容写入文件成功！")
            fh.close()

    @staticmethod
    # 写入MongoDB数据库
    def input_database():
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.test
        # 使用集合(表)
        collection = db.pracit
        # 添加单条记录到集合中
        post1 = {"_id": "1", "title": "I Love Python", "slug": "i-love-python",
                 "author": "SErHo", "content": "I Love  Python....",
                 "tags": ["Love", "Python"], "time": datetime.datetime.now()}
        post2 = {"_id": "2", "title": "Python and MongoDB", "slug": "python-mongodb", "author": "SErHo",
                 "content": "Python and MongoDB....", "tags": ["Python", "MongoDB"],
                 "time": datetime.datetime.now()}
        post3 = {"_id": "3", "title": "SErHo Blog",  "slug": "serho-blog", "author": "Akio",
                 "content": "SErHo Blog is OK....", "tags": ["SErHo", "Blog"],
                 "time": datetime.datetime.now()}
        collection.insert(post1)
        collection.insert(post2)
        collection.insert(post3)
        # 查询所有记录
        print("查询所有记录: ")
        for data in collection.find():
            print(data)
        client.close()

    @staticmethod
    # 查询MongoDB数据库

    @staticmethod
    def update_database():
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.perinfo
        collection.update()

if __name__ == '__main__':
    in1 = InputPersonData()
    # in1.writefile()
    # InputPersonData.writefile()  # 作用同上
    # InputPersonData.input_database()



