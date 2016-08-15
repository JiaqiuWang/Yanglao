"""
将老人的居住信息，先测试写入文本，再写入数据库！
"""
import pymongo
import random
import datetime


class InputPersonData:

    # 全局变量
    varString = "admin你好！"
    x = "123"
    temp_in = "data"
    # 连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client.yanglao

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
    def input_database(input_tuple):

        # 使用集合(表)
        collection = InputPersonData.db.diagnosis
        # 添加单条记录到集合中
        # money = {"_id": 3, "pPer_id": "p3", "moName": "退休金/养老金"}
        collection.insert(input_tuple)
        # 查询所有记录
        # print("查询所有记录: ")
        # for data in collection.find():
        #    print(data)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 连接指定IP地址的数据库
        client = pymongo.MongoClient("127.0.0.1", 27017)
        # 选择数据库
        db = client.yanglao
        # 使用集合(表)
        collection = db.diagnosis
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
        # 使用集合(表)
        collection = InputPersonData.db.diagnosis
        collection.remove()
        InputPersonData.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(2001, 3001):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            # print("return-var_time: ", var_time)
            dis_name = random_tuple()
            dis_id = get_value_of_dict(dis_name)
            text = {"_id": var, "pPer_id": "p3", "diseaseID": dis_name, "diseaseName": dis_id,
                    "check_time": var_time.strftime("%Y-%m-%d  %H:%M:%S")}
            print("return_text: ", text)
            InputPersonData.input_database(text)
            var += 1


def get_value_of_dict(dis_name):
    var_dict = {"D1": "糖尿病", "D2": "高血压", "D3": "慢性支气管炎", "D4":
                "冠心病", "D5": "老年痴呆", "D6": "类风湿关节炎", "D7": "脑出血", "D8": "胃溃疡"}
    temp_var_get = var_dict[dis_name]
    return temp_var_get


def random_datetime(pre, after):
    r_year = int(random.randint(pre, after))
    r_month = int(random.randint(1, 12))
    r_day = int(random.randint(1, 31))
    r_hour = int(random.randint(0, 23))
    r_min = int(random.randint(0, 59))
    r_sec = int(random.randint(0, 59))
    # print("Pre-随机生成的日期：", r_year, r_month, r_day, r_hour, r_min, r_sec)
    if (r_month == 2 or r_month == 4 or r_month == 6 or r_month == 9 or r_month == 11) and (r_day > 30):
        # print("递归调用！", r_month, r_day)
        return None
        # random_datetime(pre, after)
    elif (r_month == 2) and (r_day > 28):
        # random_datetime(pre, after)
        return None
    else:
        # print("After-随机生成的日期：", r_year, r_month, r_day, r_hour, r_min, r_sec)
        var_datetime_hit = datetime.datetime(r_year, r_month, r_day, r_hour, r_min, r_sec)
        # print("随机日期和时间hit：", var_datetime_hit)
        return var_datetime_hit


def random_tuple():
    # var_list = ["糖尿病", "高血压", "慢性支气管炎", "冠心病", "老年痴呆", "类风湿关节炎", "脑出血", "胃溃疡"]
    # var_tuple = ("糖尿病", "高血压", "慢性支气管炎", "冠心病", "老年痴呆", "类风湿关节炎", "脑出血", "胃溃疡")
    # print(random.choice(var_list))
    var_ill_id = ["D8", "D8", "D7", "D4", "D4", "D2", "D2"]
    # var_ill_id = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
    # var_dict = {"D1": "糖尿病", "D2": "高血压", "D3": "慢性支气管炎", "D4":
    # "冠心病", "D5": "老年痴呆", "D6": "类风湿关节炎", "D7": "脑出血", "D8": "胃溃疡"}
    # print(random.choice(var_dict))
    # print((var_dict.items()))
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = InputPersonData()
    # in1.writefile()
    # InputPersonData.writefile()  # 作用同上
    # InputPersonData.input_database()
    # in1.update_database()
    # in1.find_one()
    # in1.delete_one()
    # in1.delete_all()
    # in1.find_all()
    in1.write_stream_data()
    # in1.random_datetime()
    # random_tuple()
