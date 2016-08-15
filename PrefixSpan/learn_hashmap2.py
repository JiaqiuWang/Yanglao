table = {'abc':1, 'def':2, 'ghi':3}
print(table)

# 字典反转
map = dict([(v,k) for k, v in table.iteritems()])
# 字典遍历
for key in map.keys():
    print(key, ":", map[key])

print(len(map))
print(map.keys())
print(map.values())

# 字典的增，删，改，查
# 在这里需要来一句，对于字典的扩充，只需定义一个新的键值对即可，
# 而对于列表，就只能用append方法或分片赋值。
map[4] = "xyz"
print(map)

del map[4]
print(map)

map[3]="update"
print(map)

if map.has_key(1):
    print("1 key in")