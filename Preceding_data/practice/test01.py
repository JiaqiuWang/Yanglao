import random
# import datetime


def random_datetime(pre, after):
    r_year = int(random.randint(pre, after))
    r_month = int(random.randint(1, 12))
    r_day = int(random.randint(1, 31))
    r_hour = int(random.randint(0, 23))
    r_min = int(random.randint(0, 59))
    r_sec = int(random.randint(0, 59))
    print("Pre-随机生成的日期：", r_year, r_month, r_day, r_hour, r_min, r_sec)
    if (r_month == 2 or r_month == 4 or r_month == 6 or r_month == 9 or r_month == 11) and (r_day > 30):
        print("递归调用！", r_month, r_day)
        random_datetime(pre, after)
    elif(r_month == 2) and (r_day > 29):
        random_datetime(pre, after)
    else:
        print("After-随机生成的日期：", r_year, r_month, r_day, r_hour, r_min, r_sec)
    # var_datetime = datetime.datetime(r_year, r_month, r_day, r_hour, r_min, r_sec)
    # print("随机日期时间：", datetime.date(r_year, r_month, r_day))
    # print("随机日期和时间：", var_datetime)
    # print(time.strftime('Random date:%Y-%m-%d  %H:%M:%S', time.localtime(random.randint(2002, 2017))))
    # if var_datetime is not None:
    #    return var_datetime
    # else:
    #    random_datetime()

if __name__ == '__main__':
    for var in range(1, 101):
        random_datetime(2016, 2016)
