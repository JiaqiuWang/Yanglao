# 这个好，一行一行读取数据
import codecs

f = codecs.open("G1.txt", "r+", "utf-8")  # 读取中文
line = f.readline()  # 读取一行
# line.replace('\r\n', ' ')
line.strip()  # 删除字符串左右的空格

while line:
    # print("字符串长度：", len(line))
    line = line.strip('\r\n')  # 去掉每个字符的'\r\n'
    # print(line, end=" ")
    print(line.split('\t', 1))
    line = f.readline()
f.close()
