"""
将老人的居住信息，先测试写入文本，再写入数据库！
"""
import pymongo
import random
import datetime


class SpTr:

    # 全局变量-连接指定IP地址的数据库
    client = pymongo.MongoClient("127.0.0.1", 27017)
    # 获取数据库
    db = client.yanglao
    # 获取集合
    collection = db.specialtreat

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
        SpTr.collection.insert(input_tuple)

    @staticmethod
    # 查询所有collections
    def find_all():
        # 查询所有
        for data in SpTr.collection.find():
            print(data)
        print("总记录数为：", SpTr.collection.find().count())
        SpTr.client.close()

    @staticmethod
    def update_database():
        SpTr.collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        SpTr.client.close()

    @staticmethod
    def find_one():
        for u in SpTr.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            SpTr.client.close()

    @staticmethod
    def delete_one():
        for u in SpTr.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            SpTr.collection.remove({"_id": 1})
            SpTr.client.close()

    @staticmethod
    def delete_all():
        SpTr.collection.remove()
        SpTr.client.close()

    @staticmethod
    # 写一个循环生成流数据
    def write_stream_data():
        counti = 1
        for var in range(1, 1001):
            var_time = random_datetime(2013, 2016)
            while var_time is None:
                var_time = random_datetime(2013, 2016)
            # print("return-var_time: ", var_time)
            drug_id = random_tuple()
            drug_psychotropic = random_psycho()
            drug_order = random_order()
            drug_order_name = get_value_of_dict_order(drug_order)
            drug_name = get_value_of_dict(drug_id)
            da_id = random_drug_allergy()
            da_name = get_value_of_dict_drug_allergy(da_id)
            text = {"_id": var, "pPer_id": "p1", "treat_plan_id": counti, "drug_use_name": drug_name,
                    "Psychotropic": drug_psychotropic, "DoctorOrder_id": drug_order,
                    "DoctorOrder_name": drug_order_name,
                    "dDrugAllergy_id": da_id,
                    "dDrugAllergy_name": da_name,
                    "check_time": var_time.strftime("%Y-%m-%d  %H:%M:%S")}
            print("return_text: ", text)
            # 将参数传入药物使用明细collection
            SpTr.input_database(text)
            var += 1
            counti += 1

    @staticmethod
    # 读取诊断collection中的记录
    def read_diagnosis():
        collection = SpTr.db.diagnosis
        # 查询所有
        for data in collection.find():
            print(data)
            # 获取疾病对应的治疗方法
            treatplanID = get_treatplanID(data.get("diseaseID"))
            # 获取是否遵从医嘱
            treat_order = random_order()
            treat_order_name = get_value_of_dict_order(treat_order)
            text = {"_id":  data.get("_id"), "diseaseID": data.get("diseaseID"), "treat_time": data.get("check_time"),
                    "treat_plan": treatplanID, "treat_order": treat_order, "drug_order_name": treat_order_name}
            SpTr.input_database(text)
            # print("text:", text)
        print("总记录数为：", collection.find().count())
        SpTr.client.close()


def get_treatplanID(disease_id):
    # 获取集合
    collection = SpTr.db.treatmethod
    for u in collection.find({"diseaseID": disease_id}):
        print("符合条件的记录", u.get("treatplanID"))
        dict_tmp = {"treatplanID": u.get("treatplanID"), "treatplanName": u.get("treatplanName")}
        return dict_tmp


def get_value_of_dict(dis_id):
    var_dict = {"Dg1": "胰岛素", "Dg2": "硝苯地平缓释片", "Dg3": "消炎咳药", "Dg4":
                "硝酸甘油", "Dg5": "阿瑞斯", "Dg6": "抗风湿药", "Dg7": "微创置管血肿穿刺术", "Dg8": "硫糖铝"}
    # 每种药物对应治疗的疾病：{"D1": "糖尿病", "D2": "高血压", "D3": "慢性支气管炎", "D4":
    #            "冠心病", "D5": "老年痴呆", "D6": "类风湿关节炎", "D7": "脑出血", "D8": "胃溃疡"}
    treat_plan = {"tp1": "静脉注射胰岛素", "tp2": "卡托普利", "tp3": "消炎咳喘", "tp4": "注射硝酸甘油", "tp5": "麦司卡林",
                  "tp6": "风湿疗法", "tp7": "微创血管治疗", "tp8": "胃治疗"}
    temp_var_get = var_dict[dis_id]
    return temp_var_get


def get_value_of_dict_order(dis_id):
    var_dict = {"t1": "完全遵从", "t2": "不完全遵从", "t3": "出于合理原因不完全遵从", "t4":
                "不遵从"}
    temp_var_get = var_dict[dis_id]
    return temp_var_get


def get_value_of_dict_drug_allergy(dis_id):
    var_dict = {"DA0": "否", "DA1": "青霉素类", "DA2": "庆大霉素类", "DA3": "磺胺类"}
    temp_var_get = var_dict[dis_id]
    return temp_var_get


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


def random_tuple():
    var_ill_id = ["Dg1", "Dg3", "Dg5", "Dg7", "Dg5", "Dg3"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_psycho():
    var_ill_id = ["yes", "no"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_drug_allergy():
    var_ill_id = ["DA0", "DA1", "DA2", "DA3"]
    var_temp = random.choice(var_ill_id)
    return var_temp


def random_order():
    var_ill_id = ["t1", "t2", "t3", "t4"]
    var_temp = random.choice(var_ill_id)
    return var_temp

if __name__ == '__main__':
    in1 = SpTr()
    # in1.writefile()
    # InputPersonData.writefile()  # 作用同上
    # InputPersonData.input_database()
    # in1.update_database()
    # in1.find_one()
    # in1.delete_one()
    # in1.delete_all()
    in1.find_all()
    # in1.read_diagnosis()
    # in1.write_stream_data()
    # in1.random_datetime()
    # random_tuple()

