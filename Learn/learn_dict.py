dictionary = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}

# 访问字典中的值
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict3['Name']", dict3["Name"])
print("dict3['Age']", dict3["Age"])

seq = ('name', 'age', 'sex')  # 元祖
dict4 = dict.fromkeys(seq)
print("新的字典为：", dict4)

dict4 = dict.fromkeys(seq, 10)
print("新的字典为：", dict4)

print("Value :", dict3.items())
