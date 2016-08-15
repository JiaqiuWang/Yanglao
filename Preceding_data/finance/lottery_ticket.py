"""
购买彩票
"""
import pymongo
import random
import datetime


class Lottery:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.lottery
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "彩票服务"

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
        Lottery.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in Lottery.collection.find():
            print(data)
        print("总记录数为：", Lottery.collection.find().count())
        Lottery.client.close()

    @staticmethod
    def update_database():
        Lottery.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        Lottery.client.close()

    @staticmethod
    def find_one():
        for u in Lottery.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            Lottery.client.close()

    @staticmethod
    def delete_one():
        for u in Lottery.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            Lottery.collection.remove({"_id": 1})
            Lottery.client.close()

    @staticmethod
    def delete_all():
        Lottery.collection.remove()
        Lottery.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(2001, 3001):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            from_sa = random_from()
            type_lottery = random_type_lottery()
            location = random_location()
            balance = get_balance(type_lottery)
            quantity = random_quantity()
            lottery_text = {"_id": var, "pPer_id": Lottery.pPer_id, "use_time": visiting_time,
                            "from": from_sa, "service_name": Lottery.pay_name, "type": type_lottery,
                            "location": location, "balance": balance, "quantity": quantity}
            print("text: ", lottery_text)
            Lottery.input_database(lottery_text)
            # 将参数传入药物使用明细collection
            # StockBone.write_payment(payment, visiting_time, charge_ld)
            var += 1


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


def get_balance(type_lottery):
    if type_lottery == "查询中奖信息":
        balance_my = "unchanged"
    elif type_lottery == "购买彩票":
        balance_my = "expense"
    elif type_lottery == "出售彩票" or type_lottery == "领取中奖金额":
        balance_my = "income"
    else:
        balance_my = "unchanged"
    return balance_my


def random_location():
    var_ill_id = ["Home", "Home", "Home", "Home", "Community",
                  "Community", "Home", "Home", "Home",
                  "Home", "Home", "Home", "Pension Agency", "Corporation", "Mall"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_quantity():
    var_ill_id = ["medium", "medium", "medium", "multiple", "medium",
                  "medium", "medium", "medium", "single", "medium"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_type_lottery():
    var_ill_id = ["查询中奖信息", "查询中奖信息", "购买彩票", "出售彩票", "查询中奖信息", "出售彩票", "出售彩票",
                  "出售彩票", "出售彩票", "出售彩票", "出售彩票", "购买彩票", "购买彩票", "出售彩票", "领取中奖金额",
                  "领取中奖金额"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_from():
    var_ill_id = ["网易彩票", "网易彩票", "网易彩票", "网易彩票", "全民彩票", "福利彩票", "双色球",
                  "必中彩票", "网易彩票"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = Lottery()
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
