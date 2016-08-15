import FrequentSequences

list_frequent = []  # 总的列表
list_flag = []  # 用于判断的列表
# noinspection PyTypeChecker
for var_i in range(10):
    sequence = "X服务"+str(var_i)
    list_fp = [sequence]
    sup_item = 0.39
    sp = FrequentSequences.SequencesFP(list_fp, sup_item)
    list_flag.append(sp)
    list_frequent.append(sp)
    # print("var_i:", var_i, ", list_fp:", sp.sequence, ", sup_item:", sp.support)


i = 0

# while list_flag is not None:
#    for var_ta in list_flag:
#        print("sequence: ", var_ta.sequence, ", sup:", var_ta.support, ", count:", i)
#        i += 1
#    list_flag = None

# print("list.clear():", list_flag.clear())

for var_seq in list_flag:
    print("sequence:", var_seq.sequence, ", support:", var_seq.support)
list_flag.clear()


