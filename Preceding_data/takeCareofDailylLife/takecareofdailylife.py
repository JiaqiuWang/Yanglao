"""
将老人的预约挂号信息，写入数据库！
"""
import pymongo
import random
import datetime


class TDL:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.dailylife
    # 用户标识
    pPer_id = "p1"
    # 支付名称
    pay_name = "照料饮食起居服务"

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
        TDL.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in TDL.collection.find():
            print(data)
        print("总记录数为：", TDL.collection.find().count())
        TDL.client.close()

    @staticmethod
    def update_database():
        TDL.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        TDL.client.close()

    @staticmethod
    def find_one():
        for u in TDL.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            TDL.client.close()

    @staticmethod
    def delete_one():
        for u in TDL.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            TDL.collection.remove({"_id": 1})
            TDL.client.close()

    @staticmethod
    def delete_all():
        TDL.collection.remove()
        TDL.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(1, 151):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d")
            duration = random_duration()
            charge_ld = duration+"费用"
            from_sa = random_from()
            payment = "takecaredaily_"+str(var)
            daily_life = {"_id": var, "pPer_id": TDL.pPer_id, "start_date": visiting_time,
                          "duration": duration, "service_name": TDL.pay_name,
                          "charge": charge_ld, "from": from_sa, "payment": payment}
            print("text: ", daily_life)
            TDL.input_database(daily_life)
            # 将参数传入药物使用明细collection
            TDL.write_payment(payment, visiting_time, charge_ld)
            var += 1

    @staticmethod
    # 写一个循环生成流数据
    def write_payment(payment, visiting_time, charge):
        # 获取集合
        collection = TDL.db.payment
        # 获取支付id
        payment_id = get_var_id()
        from_app = random_pay_service()
        payment_text = {"_id": payment_id, "pPer_id": TDL.pPer_id, "pay_ID": payment, "pay_time": visiting_time,
                        "pay_fee": charge, "from": from_app,
                        "pay_name": TDL.pay_name}
        print("payment_text: ", payment_text)
        collection.insert(payment_text)


def get_var_id():
    # 获取集合
    collection = TDL.db.payment
    cursor_count = collection.find().count()
    cursor_count += 1
    return cursor_count


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


def random_duration():
    var_ill_id = ["1天", "2天", "3天", "4天", "5天", "1周", "2周", "2天"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_from():
    var_ill_id = ["百善网", "智慧养老", "web_yang_lao"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pay_service():
    # var_ill_id = ["Alipay", "Wechat", "Credit Card",  "PayPal"]
    var_ill_id = ["Alipay", "PayPal", "PayPal", "PayPal", "Alipay", "银联支付"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = TDL()
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
