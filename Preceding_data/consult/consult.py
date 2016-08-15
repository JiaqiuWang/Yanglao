"""
咨询服务！
"""
import pymongo
import random
import datetime


class Consult:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.consult
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "咨询服务"

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
        Consult.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in Consult.collection.find():
            print(data)
        print("总记录数为：", Consult.collection.find().count())
        Consult.client.close()

    @staticmethod
    def update_database():
        Consult.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        Consult.client.close()

    @staticmethod
    def find_one():
        for u in Consult.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            Consult.client.close()

    @staticmethod
    def delete_one():
        for u in Consult.collection.find({"pPer_id": "p2"}):
            # print("符合条件的记录(_id:1 ): ", u)
            Consult.collection.remove({"pPer_id": "p2"})
            Consult.client.close()

    @staticmethod
    def delete_all():
        Consult.collection.remove()
        Consult.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(2001, 3001):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            from_sa = random_from()
            type_consult = random_type_consult(from_sa)
            location = random_location()
            consult_text = {"_id": var, "pPer_id": Consult.pPer_id, "order_time": visiting_time,
                            "from": from_sa, "service_name": Consult.pay_name, "type": type_consult,
                            "location": location}
            print("text: ", consult_text)
            Consult.input_database(consult_text)
            # 将参数传入药物使用明细collection
            # Consult.write_payment(payment, visiting_time, charge_ld)
            var += 1


def get_deliver_address(type_express):
    if type_express == "蔬菜" or type_express == "水果" or type_express == "桶装水":
        deliver_add = "Pension Agency"
    else:
        deliver_add = "Home"
    return deliver_add


def get_charge_quantity(quantity):
    if quantity == "more":
        charge = "high"
    else:
        charge = "low"
    return charge


def random_datetime(pre, after):
    r_year = int(random.randint(pre, after))
    r_month = int(random.randint(1, 12))
    r_day = int(random.randint(1, 31))
    r_hour = int(random.randint(6, 20))
    r_min = int(random.randint(0, 59))
    r_sec = int(random.randint(0, 59))
    if (r_month == 2 or r_month == 4 or r_month == 6 or r_month == 9 or r_month == 11) and (r_day > 30):
        return None
    elif (r_month == 2) and (r_day > 28):
        return None
    else:
        var_datetime_hit = datetime.datetime(r_year, r_month, r_day, r_hour, r_min, r_sec)
        return var_datetime_hit


def random_quantity():
    var_ill_id = ["more", "less", "more", "less", "more", "less", "more", "more"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_type_consult(from_sa):
    if from_sa == "房产法律咨询" or from_sa == "财产法律咨询" or from_sa == "婚姻法律咨询":
        type_consult = "法律咨询"
    elif from_sa == "养生咨询" or from_sa == "健康咨询" or from_sa == "锻炼咨询":
        type_consult = "健康养生"
    else:
        type_consult = "求医问药"
    return type_consult


def random_from():
    var_ill_id = ["财产法律咨询", "财产法律咨询", "财产法律咨询", "健康咨询", "健康咨询", "健康咨询",
                  "健康咨询", "锻炼咨询", "健康咨询", "健康咨询", "财产法律咨询", "财产法律咨询", "财产法律咨询",
                  "问药", "财产法律咨询", "财产法律咨询", "心理咨询", "财产法律咨询"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_location():
    var_ill_id = ["Home", "Pension Agency", "Community", "Pension Agency",
                  "Pension Agency", "Pension Agency", "Home", "Community"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = Consult()
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
    # random_termination_point("Hospital")
