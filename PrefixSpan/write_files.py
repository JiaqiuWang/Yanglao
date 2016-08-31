import codecs

# with open("out_print.txt", "w") as f:
#     f.write("nhee\n")
#     f.close()

a = 34
f = codecs.open('out_print.txt', 'a+', 'utf-8')
f.write('中文'+str(a))
f.write("\n")
f.close()
