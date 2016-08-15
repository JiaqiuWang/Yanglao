import re

print(re.match('www', 'www.hello.com').span())  # 在起始位置匹配
print(re.match('come', 'www.hello.com'))        # 不在起始位置匹配

line = "Cats are smarter than dogs"
matchObj = re.match('(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

line2 = "check_time"

matchObj2 = re.match('(.*)_date|(.*)_time', line2, re.M | re.I)
if matchObj2:
    print("matchObj2.group() : ", matchObj2.group())
    print("matchObj2.group(1) : ", matchObj2.group(1))
else:
    print("No match!!")
