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
print("Value :", dict3.items())

# 测试把list设定为字典数据结构的key
list2 = ['支付服务', '精神慰藉服务']
list_index = [358, 369, 407, 531, 600, 697, 937, 1044, 1191, 1391, 1472, 1521]
dict3.setdefault(tuple(list2), list_index)

print("测试把list设定为字典数据结构的key\ndict3: ", dict3)
tuple_key = tuple(list2)
print("tuple_key:", tuple_key, ", type:", type(tuple_key))

sequence = []
for x in tuple_key:
    print("x in tuple:", x, ", type:", type(x))
    sequence.append(x)
print("tuple is converted to list:", sequence)

