

table = {'abc': 1, 'def': 2, 'ghi': 3}
print("table:", table)

# 字典遍历
for key in table.keys():
    print(key, ":", table[key])

print(len(table))
print(table.keys())
print(table.values())

# 增加字典
table["id4"] = "xyz"
print(table)

# 删除字典
del table["id4"]
print("after delete table: ", table)

# 修改字典, 如果没有则新添加
table["adcd"] = 5
print("after update table: ", table)

if "abc" in table:
    print("table has key abc!")


