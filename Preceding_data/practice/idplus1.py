"""
将老人的预约挂号信息，写入数据库！
"""
import pymongo
import random
import datetime


class HA:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.idplusone
    # 用户标识
    pPer_id = "p1"

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
        print('----------------')

    @staticmethod
    # 写入MongoDB数据库
    def input_database(input_tuple):
        # 添加单条记录到集合中
        HA.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in HA.collection.find():
            print(data)
        print("总记录数为：", HA.collection.find().count())
        HA.client.close()

    @staticmethod
    def update_database():
        HA.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        HA.client.close()

    @staticmethod
    def find_one():
        for u in HA.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            HA.client.close()

    @staticmethod
    def delete_one():
        for u in HA.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            HA.collection.remove({"_id": 1})
            HA.client.close()

    @staticmethod
    def delete_all():
        HA.collection.remove()
        HA.client.close()

    @staticmethod
    def get_var_id():
        cursor_count = HA.collection.find().count()
        if cursor_count == 0:
            cursor_count = 1
            return cursor_count
        else:
            return cursor_count

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        var_id = get_var_id()
        for var in range(1, 101):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            hospital_id = random_hospital()
            visiting_time = var_time.strftime("%Y-%m-%d")
            disease_office = random_disease_office()

            gua_hao = {"_id": var_id, "pPer_id": HA.pPer_id, "visiting_time": visiting_time,
                       "hospital_id": hospital_id, "location": "hospital",
                       "disease_office": disease_office}
            var_id += 1
            print("text: ", gua_hao)


def random_datetime(pre, after):
    r_year = int(random.randint(pre, after))
    r_month = int(random.randint(1, 12))
    r_day = int(random.randint(1, 31))
    r_hour = int(random.randint(0, 23))
    r_min = int(random.randint(0, 59))
    r_sec = int(random.randint(0, 59))
    if (r_month == 2 or r_month == 4 or r_month == 6 or r_month == 9 or r_month == 11) and (r_day > 30):
        return None
    elif (r_month == 2) and (r_day > 28):
        return None
    else:
        var_datetime_hit = datetime.datetime(r_year, r_month, r_day, r_hour, r_min, r_sec)
        return var_datetime_hit


def random_hospital():
    var_ill_id = ["HP1", "HP2", "HP3", "HP4", "HP1", "HP4", "HP4", "HP4"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_disease_office():
    var_ill_id = ["D1", "D3", "D5", "D7", "D3", "D5", "D5", "D1", "D6"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def get_var_id():
    # 获取集合
    collection = HA.db.guahao
    cursor_count = collection.find().count()
    cursor_count += 1
    return cursor_count

if __name__ == '__main__':
    in1 = HA()
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
    # in1.get_var_id()

