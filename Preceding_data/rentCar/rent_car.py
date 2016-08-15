"""
将老人的预约挂号信息，写入数据库！
"""
import pymongo
import random
import datetime


class RC:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.rentcar
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "租车服务"

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
        RC.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in RC.collection.find():
            print(data)
        print("总记录数为：", RC.collection.find().count())
        RC.client.close()

    @staticmethod
    def update_database():
        RC.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        RC.client.close()

    @staticmethod
    def find_one():
        for u in RC.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            RC.client.close()

    @staticmethod
    def delete_one():
        for u in RC.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            RC.collection.remove({"_id": 1})
            RC.client.close()

    @staticmethod
    def delete_all():
        RC.collection.remove()
        RC.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(1891, 2841):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            start_point = random_start_point()
            termination_point = random_termination_point(start_point)
            charge = get_charge_rent_car(start_point, termination_point)
            from_sa = random_from()
            payment = "rentCar_"+str(var)
            rent_car = {"_id": var, "pPer_id": RC.pPer_id, "rent_time": visiting_time,
                        "start_point": start_point, "end_point": termination_point,
                        "charge": charge, "from": from_sa, "payment": payment}
            print("text: ", rent_car)
            RC.input_database(rent_car)
            # 将参数传入药物使用明细collection
            RC.write_payment(payment, visiting_time, charge)
            var += 1

    @staticmethod
    # 写一个循环生成流数据
    def write_payment(payment, visiting_time, charge):
        # 获取集合
        collection = RC.db.payment
        # 获取支付id
        payment_id = get_var_id()
        from_app = random_pay_service()
        payment_text = {"_id": payment_id, "pPer_id": RC.pPer_id, "pay_ID": payment, "pay_time": visiting_time, "pay_fee": charge,
                        "from": from_app, "pay_name": RC.pay_name}
        print("payment_text: ", payment_text)
        collection.insert(payment_text)


def get_var_id():
    # 获取集合
    collection = RC.db.payment
    cursor_count = collection.find().count()
    cursor_count += 1
    return cursor_count


def get_charge_rent_car(start_point, end_point):
    charge = 20
    if (start_point == "Home") or (end_point == "Home"):
        if (start_point == "Corporation") or (end_point == "Corporation"):
            charge = 15
    if (start_point == "Home") or (end_point == "Home"):
        if (start_point == "Hospital") or (end_point == "Hospital"):
            charge = 20
    if (start_point == "Home") or (end_point == "Home"):
        if (start_point == "Mall") or (end_point == "Mall"):
            charge = 25
    if (start_point == "Home") or (end_point == "Home"):
        if (start_point == "Garden") or (end_point == "Garden"):
            charge = 30
    if (start_point == "Corporation") or (end_point == "Corporation"):
        if (start_point == "Hospital") or (end_point == "Hospital"):
            charge = 26
    if (start_point == "Corporation") or (end_point == "Corporation"):
        if (start_point == "Mall") or (end_point == "Mall"):
            charge = 18
    if (start_point == "Corporation") or (end_point == "Corporation"):
        if (start_point == "Garden") or (end_point == "Garden"):
            charge = 23
    if (start_point == "Hospital") or (end_point == "Hospital"):
        if (start_point == "Garden") or (end_point == "Garden"):
            charge = 22
    if (start_point == "Hospital") or (end_point == "Hospital"):
        if (start_point == "Mall") or (end_point == "Mall"):
            charge = 13
    if (start_point == "Mall") or (end_point == "Mall"):
        if (start_point == "Garden") or (end_point == "Garden"):
            charge = 17
    return charge


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


def random_from():
    var_ill_id = ["滴滴出行", "滴滴出行", "web_rent_car"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pay_service():
    # var_ill_id = ["Alipay", "Wechat", "Credit Card",  "PayPal"]
    var_ill_id = ["云闪付", "Credit Card"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_start_point():
    var_ill_id = ["Home", "Hospital",  "Hospital", "Hospital", "Mall", "Hospital", "Garden", "Mall", "Mall"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_termination_point(start_point):
    list_random = ["Home", "Home", "Hospital",  "Hospital", "Hospital", "Mall", "Hospital", "Garden"]
    i = 0
    while i < len(list_random):
        if list_random[i] == start_point:
            list_random.pop(i)
            i -= 1
        else:
            print("list_random[", i, "]: ", list_random[i])
        i += 1
    # print(list_random)
    var_temp = random.choice(list_random)
    return var_temp


if __name__ == '__main__':
    in1 = RC()
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
