

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = [2, 1, 96, 45, 23, 9, 100, 0, 64]

count = 1


def find_prefix_subset(fp):
    list_5 = fp[1:]

    return list_5


while list1 is not None:
    print("list1 is not None!")
    fp_candidate_duplicate = list1.copy()  # 复制上一步新生成的频繁序列模式
    list1.clear()  # 先清空，再看是否后续扫描具有新添加的频繁序列模式
    list1 = find_prefix_subset(fp_candidate_duplicate)
    fp_candidate_duplicate.clear()  # 等找完新的一轮频繁序列模式后，再清空复制的副本
print("算法终止！")






