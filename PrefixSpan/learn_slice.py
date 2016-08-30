# myslice = slice(5)
# print(myslice)
#
# l = list(range(10))
# print(l[myslice])

myslice2 = slice(0, -1)
print(myslice2)

list_3 = ['支付服务', '刮花服务', "体育服务"]
print(list_3[myslice2])



myslice3 = slice(0, -1)
print(myslice3)

tuple_sequn = {'支付服务', '刮花服务', "体育服务"}
print(tuple_sequn[myslice3])

tuple_sequn = tuple_sequn
print("tupple_sequn:", tuple_sequn)
