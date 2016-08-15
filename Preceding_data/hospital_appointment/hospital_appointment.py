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
    collection = db.guahao
    # 用户标识
    pPer_id = "p3"

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
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(801, 1201):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            hospital_id = random_hospital()
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            disease_office = random_disease_office()
            doctor = random_doctor()
            charge = get_value_of_dict_charge(doctor)
            from_sa = random_from()
            payment = "guahao_"+str(var)
            gua_hao = {"_id": var, "pPer_id": HA.pPer_id, "visiting_time": visiting_time,
                       "hospital_id": hospital_id, "location": "hospital",
                       "disease_office": disease_office, "doctor": doctor, "charge": charge,
                       "from": from_sa, "payment": payment}
            print("text: ", gua_hao)
            HA.input_database(gua_hao)
            # 将参数传入药物使用明细collection
            HA.write_payment(payment, visiting_time, charge)
            var += 1

    @staticmethod
    # 写一个循环生成流数据
    def write_payment(payment, visiting_time, charge):
        # 获取集合
        collection = HA.db.payment
        # 获取支付id
        payment_id = get_var_id()
        from_app = random_pay_service()
        payment_text = {"_id": payment_id, "pPer_id": HA.pPer_id, "pay_ID": payment, "pay_time": visiting_time, "pay_fee": charge,
                        "from": from_app, "pay_name": "挂号服务"}
        # print("payment_text: ", payment_text)
        collection.insert(payment_text)


def get_var_id():
    # 获取集合
    collection = HA.db.payment
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


def random_hospital():
    var_ill_id = ["HP1", "HP2", "HP3", "HP4", "HP1", "HP4", "HP4", "HP4"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_disease_office():
    var_ill_id = ["D1", "D3", "D5", "D7", "D3", "D5", "D5", "D1", "D6"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_doctor():
    var_ill_id = ["主治医师", "普通号", "专家"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def get_value_of_dict_charge(dis_name):
    var_dict = {"主治医师": "10元", "普通号": "5元", "专家": "15元"}
    temp_var_get = var_dict[dis_name]
    return temp_var_get


def random_from():
    var_ill_id = ["春雨医生App", "微医App", "web挂号", "web挂号", "web挂号", "web挂号", "web挂号"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_pay_service():
    var_ill_id = ["Alipay", "Wechat", "Credit Card",  "PayPal"]
    var_temp = random.choice(var_ill_id)
    return var_temp


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
