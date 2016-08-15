"""
快递服务！送大米，鸡蛋，食用油，蔬菜，水果，外卖
"""
import pymongo
import random
import datetime


class Express:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.express
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "快递服务"

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
        Express.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in Express.collection.find().sort({"order_time": 1}):
            print(data)
        print("总记录数为：", Express.collection.find().count())
        Express.client.close()

    @staticmethod
    def update_database():
        Express.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        Express.client.close()

    @staticmethod
    def find_one():
        for u in Express.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            Express.client.close()

    @staticmethod
    def delete_one():
        for u in Express.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            Express.collection.remove({"_id": 1})
            Express.client.close()

    @staticmethod
    def delete_all():
        Express.collection.remove()
        Express.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(1601, 2401):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            from_sa = random_from()
            type_express = random_type_express()
            deliver_add = get_deliver_address(type_express)
            quantity = random_quantity()
            charge_ld = get_charge_quantity(quantity)
            payment = "express_"+str(var)
            daily_life = {"_id": var, "pPer_id": Express.pPer_id, "order_time": visiting_time,
                          "from": from_sa, "service_name": Express.pay_name, "type": type_express,
                          "deliver_address": deliver_add,
                          "quantity": quantity,"charge": charge_ld, "payment": payment}
            print("text: ", daily_life)
            Express.input_database(daily_life)
            # 将参数传入药物使用明细collection
            Express.write_payment(payment, visiting_time, charge_ld)
            var += 1

    @staticmethod
    # 写一个循环生成流数据
    def write_payment(payment, visiting_time, charge):
        # 获取集合
        collection = Express.db.payment
        # 获取支付id
        payment_id = get_var_id()
        from_app = random_pay_service()
        payment_text = {"_id": payment_id, "pPer_id": Express.pPer_id, "pay_ID": payment, "pay_time": visiting_time,
                        "pay_fee": charge, "from": from_app,
                        "pay_name": Express.pay_name}
        print("payment_text: ", payment_text)
        collection.insert(payment_text)


def get_var_id():
    # 获取集合
    collection = Express.db.payment
    cursor_count = collection.find().count()
    cursor_count += 1
    return cursor_count


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


def random_type_express():
    var_ill_id = ["蔬菜", "蔬菜", "水果", "水果", "桶装水", "水果", "水果", "鸡蛋",
                  "水果", "白面"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_from():
    var_ill_id = ["闪电购", "闪电购", "社区快递", "社区快递", "社区快递", "社区快递",
                  "超级快递"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pay_service():
    var_ill_id = ["云闪付", "Credit Card", "百度钱包", "Credit Card", "Credit Card"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = Express()
    # in1.writefile()
    # InputPersonData.writefile()  # 作用同上
    # InputPersonData.input_database()
    # in1.update_database()
    # in1.find_one()
    # in1.delete_one()
    # in1.delete_all()
    in1.find_all()
    # in1.write_stream_data()
    # in1.random_datetime()
    # random_tuple()
    # random_termination_point("Hospital")
