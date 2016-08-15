list1 = ['Google', 'Run', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a", "b", "c", "d"]

print("list1[0]:", list1[0])
for i in list1:
    print("I:", i)


print("list2[1:5]:", list2[1:5])

# 对列表的数据项进行更新
print("第三个元素为：", list1[2])
list1[2] = 2001
print("更新后的第三个元素为：", list1[2])
print("list3[-2]:", list3[-2])  # 从右侧开始读取倒数第二个元素
print("list1+list2:", list1+list2)
print("list1[1:]:", list1[1:])

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("x: ", x)
print("x[0]: ", x[0])
print("x[0][1]: ", x[0][1])
print("列表元素：len(list): ", len(x))
print("列表元素的最大值：(max(list)): ", max(a), " anther: ", max(n))
print("列表元素的最大值：(min(list)): ", min(a), " anther: ", min(n))

a_list = [123, 'xyz', 'zara', 'abc', '123']
a_list.append(2009)
print("updated list: ", a_list)

aList = [123, 'Google', 'Runoob', 'Taobao', 123]
print("123 元素的个数：", aList.count(123))
print("Taobao 元素的个数：", aList.count("Taobao"))

list4 = list(range(5))
print("list4: ", list4)
list1.extend(list4)
print("扩展后的列表：", list1)

print("Run 的索引位置值：", list1.index("Run"))
# print("Rate 的索引位置值：", list1.index("Rate"))  # 抛出异常，如果队列中没有该元素

# insert()函数用于将制定对象插入到列表中的指定位置 list.insert(index, obj)
list3.insert(1, "Bate")
print("列表插入元素后为：", list3)

# pop()
list3.pop()
print("移除pop后的列表List3为：", list3)
list3.pop(1)
print("移除pop后的列表List3为：", list3)

# remove() 函数用于移除列表中某个值的第一个匹配项。
aList.remove("Taobao")
print("aList的Taobao:,", aList)

# reverse() 函数用于反向列表中元素。
aList.reverse()
print(aList)

# sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。 list.sort([func])
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = [2, 1, 96, 45, 23, 9, 100, 0, 64]
print("slice: list2[3:6]", list2[3:6])

list1.sort()
list2.sort()
print("列表排序后 : ", list1)
print("列表排序后 : ", list2)
print("slice: list2[3:6]", list2[3:6])

# clear() 函数用于清空列表，类似于 del a[:]。
list1.clear()
print("列表清空后 : ", list1)

# copy() 函数用于复制列表，类似于 a[:]。
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print("list2 列表: ", list2)

list5 = range(5, 25, 5)
print("list5: ", list5[3:5])

service_name = 'Google'
if service_name not in list1:
    print("service_name:", service_name, " is not in list1:", list1)

list1 = ["支付服务"]
str2 = "用药服务"
list3 = [str2]
print("list3:", list3)
print("list2:", str2)
list1.extend(list3)
print("extended list1:", list1)
# print(list1+list3)
list1 = ["支付服务"]
print("修改后的list1:", list1)


list1 = ["支付服务", "兴大服务", "打了服务"]
list1 = ["asdg"]
print("list1:", list1)


