"""
快递服务！送大米，鸡蛋，食用油，蔬菜，水果，外卖
"""
import pymongo
import random
import datetime


class TakeOut:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.takeout
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "外卖服务"

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
        TakeOut.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in TakeOut.collection.find():
            print(data)
        print("总记录数为：", TakeOut.collection.find().count())
        TakeOut.client.close()

    @staticmethod
    def update_database():
        TakeOut.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        TakeOut.client.close()

    @staticmethod
    def find_one():
        for u in TakeOut.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            TakeOut.client.close()

    @staticmethod
    def delete_one():
        for u in TakeOut.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            TakeOut.collection.remove({"_id": 1})
            TakeOut.client.close()

    @staticmethod
    def delete_all():
        TakeOut.collection.remove()
        TakeOut.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(1601, 2401):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            from_sa = random_from()
            type_take_out = random_type_takeout()
            deliver_add = random_deliver_address()
            quantity = random_quantity()
            charge_ld = get_charge_quantity(quantity)
            payment = "express_"+str(var)
            daily_life = {"_id": var, "pPer_id": TakeOut.pPer_id, "order_time": visiting_time,
                          "from": from_sa, "service_name": TakeOut.pay_name, "typeTakeout": type_take_out,
                          "deliver_address": deliver_add,
                          "quantity": quantity, "charge": charge_ld, "payment": payment}
            print("text: ", daily_life)
            TakeOut.input_database(daily_life)
            # 将参数传入药物使用明细collection
            TakeOut.write_payment(payment, visiting_time, charge_ld)
            var += 1

    @staticmethod
    # 写一个循环生成流数据
    def write_payment(payment, visiting_time, charge):
        # 获取集合
        collection = TakeOut.db.payment
        # 获取支付id
        payment_id = get_var_id()
        from_app = random_pay_service()
        payment_text = {"_id": payment_id, "pPer_id": TakeOut.pPer_id, "pay_ID": payment, "pay_time": visiting_time,
                        "pay_fee": charge, "from": from_app,
                        "pay_name": TakeOut.pay_name}
        print("payment_text: ", payment_text)
        collection.insert(payment_text)


def get_var_id():
    # 获取集合
    collection = TakeOut.db.payment
    cursor_count = collection.find().count()
    cursor_count += 1
    return cursor_count


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
    r_hour = int(random.randint(10, 14))
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
    var_ill_id = ["more", "more", "more", "less", "more", "more", "more", "more", "less"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_deliver_address():
    var_ill_id = ["Home", "Pension Agency", "Community", "Pension Agency",
                  "Pension Agency", "Pension Agency", "Home", "Community"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_type_takeout():
    var_ill_id = ["烧烤", "烧烤", "炒菜", "麻辣烫", "麻辣烫", "麻辣烫", "盖饭", "盖饭", "盖饭",
                  "KFC鸡翅", "麻辣烫"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_from():
    var_ill_id = ["肯德基", "必胜客", "必胜客", "超级外卖", "百度外卖", "饿了么", "百度外卖",
                  "口碑外卖", "必胜客", "必胜客"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pay_service():
    var_ill_id = ["云闪付", "Credit Card", "百度钱包", "Credit Card", "Credit Card"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = TakeOut()
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
