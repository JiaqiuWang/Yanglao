import re

line = "Cats are smarter than dogs"

matchObj = re.match('dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

matchObj = re.search('dogs', line, re.M | re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

phone = "2004-959-559 # 这是一个电话号码"
num = re.sub('#.*$', "", phone)
print ("电话号码 : ", num)

# 移除非数字的内容
num = re.sub('\D', "", phone)
print ("电话号码 : ", num)
