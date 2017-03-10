import re

pattern = "www"
var_str = "www.runoob.com"
pattern_2 = "com"
var_str_2 = "www.runoob.com"
print("在起始位置匹配：", re.match(pattern, var_str).span())
print("不在起始位置匹配：", re.match(pattern_2, var_str_2))

line = "Cats are smarter than dogs"
match_obj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if match_obj:
    print("match_obj.group():", match_obj.group())
    print("matchObj.group(0, 1, 2) : ", match_obj.group(0, 1, 2))
    print("matchObj.group(1) : ", match_obj.group(1))
    print("matchObj.group(2) : ", match_obj.group(2))
    # print("matchObj.group(3) : ", match_obj.group(3))
else:
    print("No Match!")

# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

line2 = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line2, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

line3 = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)  # 匹配多行，大小写
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
    

