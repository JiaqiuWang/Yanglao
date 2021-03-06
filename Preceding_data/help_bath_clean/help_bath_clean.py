"""
助洁助浴服务！
"""
import pymongo
import random
import datetime


class HBC:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.bathclean
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "助洁助浴服务"

    # 构造函数
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.name = 'admin'

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
        HBC.client.close()

    @classmethod
    def test2(cls):
        print(cls)
        print('test2')
        print('----------------')

    @staticmethod
    # 写入MongoDB数据库
    def input_database(input_tuple):
        # 添加单条记录到集合中
        HBC.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in HBC.collection.find():
            print(data)
        print("总记录数为：", HBC.collection.find().count())
        HBC.client.close()

    @staticmethod
    def update_database():
        HBC.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        HBC.client.close()

    @staticmethod
    def find_one():
        for u in HBC.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            HBC.client.close()

    @staticmethod
    def delete_one():
        for u in HBC.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            HBC.collection.remove({"_id": 1})
            HBC.client.close()

    @staticmethod
    def delete_all():
        HBC.collection.remove()
        HBC.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(761, 1141):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            from_sa = random_from()
            location = get_location(from_sa)
            charge_ld = from_sa+"费用"
            payment = "bathclean_"+str(var)
            daily_life = {"_id": var, "pPer_id": HBC.pPer_id, "start_date": visiting_time,
                          "service_name": HBC.pay_name, "from": from_sa, "location": location,
                          "charge": charge_ld,  "payment": payment, }
            print("text: ", daily_life)
            HBC.input_database(daily_life)
            # 将参数传入药物使用明细collection
            HBC.write_payment(payment, visiting_time, charge_ld)
            var += 1

    @staticmethod
    # 写一个循环生成流数据
    def write_payment(payment, visiting_time, charge):
        # 获取集合
        collection = HBC.db.payment
        # 获取支付id
        payment_id = get_var_id()
        from_app = random_pay_service()
        payment_text = {"_id": payment_id, "pPer_id": HBC.pPer_id, "pay_ID": payment, "pay_time": visiting_time,
                        "pay_fee": charge, "from": from_app,
                        "pay_name": HBC.pay_name}
        print("payment_text: ", payment_text)
        collection.insert(payment_text)


def get_var_id():
    # 获取集合
    collection = HBC.db.payment
    cursor_count = collection.find().count()
    cursor_count += 1
    return cursor_count


def get_location(from_sa):
    # 获取集合
    location = "Home"
    if from_sa == "老人助洁":
        location = "Community"
    if from_sa == "养老清洁" or from_sa == "web_yang_lao":
        location = "Pension Agency"
    return location


def random_datetime(pre, after):
    r_year = int(random.randint(pre, after))
    r_month = int(random.randint(1, 12))
    r_day = int(random.randint(1, 31))
    r_hour = int(random.randint(18, 21))
    r_min = int(random.randint(0, 59))
    r_sec = int(random.randint(0, 59))
    if (r_month == 2 or r_month == 4 or r_month == 6 or r_month == 9 or r_month == 11) and (r_day > 30):
        return None
    elif (r_month == 2) and (r_day > 28):
        return None
    else:
        var_datetime_hit = datetime.datetime(r_year, r_month, r_day, r_hour, r_min, r_sec)
        return var_datetime_hit


def random_from():
    var_ill_id = ["老人助洁", "养老清洁", "老人助洁", "老人助洁", "养老清洁", "web_yang_lao", "web_yang_lao"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pay_service():
    var_ill_id = ["云闪付", "Credit Card", "百度钱包", "Credit Card", "Credit Card"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = HBC()
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
