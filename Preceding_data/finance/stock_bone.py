"""
购买股票，债券，基金等服务
"""
import pymongo
import random
import datetime


class StockBone:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.stock
    # 用户标识
    pPer_id = "p3"
    # 支付名称
    pay_name = "股票债券服务"

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
        StockBone.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in StockBone.collection.find():
            print(data)
        print("总记录数为：", StockBone.collection.find().count())
        StockBone.client.close()

    @staticmethod
    def update_database():
        StockBone.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        StockBone.client.close()

    @staticmethod
    def find_one():
        for u in StockBone.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            StockBone.client.close()

    @staticmethod
    def delete_one():
        for u in StockBone.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            StockBone.collection.remove({"_id": 1})
            StockBone.client.close()

    @staticmethod
    def delete_all():
        StockBone.collection.remove()
        StockBone.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        for var in range(201, 301):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            visiting_time = var_time.strftime("%Y-%m-%d %H:%M:%S")
            from_sa = random_from()
            type_lottery = random_type_lottery()
            location = random_location()

            stock_text = {"_id": var, "pPer_id": StockBone.pPer_id, "use_time": visiting_time,
                          "from": from_sa, "service_name": StockBone.pay_name, "type": type_lottery,
                          "location": location, }
            print("text: ", stock_text)
            StockBone.input_database(stock_text)
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


def random_location():
    var_ill_id = ["Home", "Community", "Community", "Community", "Community",
                  "Community", "Community", "Community",
                  "Pension Agency", "Home", "Home", "Home", "Corporation", "Mall"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_type_lottery():
    var_ill_id = ["查询中奖信息", "购买彩票", "领取中奖金额", "出售彩票", "查询中奖信息", "查询中奖信息", "查询中奖信息",
                  "查询中奖信息", "购买彩票", "购买彩票", "购买彩票", "购买彩票", "购买彩票", "购买彩票", "领取中奖金额"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_from():
    var_ill_id = ["福利彩票", "福利彩票", "福利彩票", "必中彩票", "双色球", "福利彩票", "双色球"]
    var_temp = random.choice(var_ill_id)
    return var_temp


if __name__ == '__main__':
    in1 = StockBone()
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
