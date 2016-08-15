"""
将老人的居住信息，先测试写入文本，再写入数据库！
"""
import pymongo
import random
import datetime


class DrugUse:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.capability

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
        DrugUse.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in DrugUse.collection.find():
            print(data)
        print("总记录数为：", DrugUse.collection.find().count())
        DrugUse.client.close()

    @staticmethod
    def update_database():
        DrugUse.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        DrugUse.client.close()

    @staticmethod
    def find_one():
        for u in DrugUse.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            DrugUse.client.close()

    @staticmethod
    def delete_one():
        for u in DrugUse.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            DrugUse.collection.remove({"_id": 1})
            DrugUse.client.close()

    @staticmethod
    def delete_all():
        DrugUse.collection.remove()
        DrugUse.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(201, 301):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            weight = random_weight()
            waistline = random_waistline()
            temperature = random_temperature()
            pulse = random_pulse()
            blood_pressure = random_blood_pressure()
            overall = random_overall()
            self_care = random_self_care()
            psychosis = random_psychosis()
            text = {"_id": var, "pPer_id": "p3", "height": "173 cm", "weight": weight,
                    "waistline": waistline, "temperature": temperature, "pulse": pulse,
                    "blood_pressure": blood_pressure, "overall": overall, "selfcare": self_care,
                    "psychosis": psychosis,
                    "check_time": var_time.strftime("%Y-%m-%d  %H:%M:%S")}
            print("text: ", text)
            # 将参数传入药物使用明细collection
            DrugUse.input_database(text)
            var += 1


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


def random_weight():
    var_ill_id = ["71.5", "71", "72", "70", "69.5", "69", "72.5", "70"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_waistline():
    var_ill_id = ["73.5", "73", "73.9", "74", "72.8", "73.5", "72.7", "73.5"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_temperature():
    var_ill_id = ["36", "36.5", "37", "36", "36.5", "36.5", "37", "38", "38.5", "37", "36.5", "38.5", "36.5"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pulse():
    var_ill_id = ["65", "70", "75", "80", "85", "90", "95", "100", "69", "83", "120", "53", "96"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_blood_pressure():
    var_ill_id = ["正常", "正常", "正常", "正常", "正常", "正常", "正常", "高血压", "低血压", "正常", "正常", "正常"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_overall():
    var_ill_id = ["健康良好", "健康受损", "健康良好", "健康良好", "健康良好", "健康良好", "健康良好", "健康受损"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_self_care():
    var_ill_id = ["完全自理", "部分自理", "无自理能力", "部分自理", "部分自理", "部分自理", "部分自理", "部分自理"
                  "完全自理", "部分自理", "部分自理"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_psychosis():
    var_ill_id = ["良好", "受损", "良好", "良好", "良好", "良好", "良好"]
    var_temp = random.choice(var_ill_id)
    return var_temp

if __name__ == '__main__':
    in1 = DrugUse()
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
