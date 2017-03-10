
# foo = open("G4.txt", "wb")  先生成一个文本文件来确定文件的位置

import os

with open("G1.txt", 'rt') as handle:
    for line in filter(None, handle):
        print(os.path.splitext(line)[0])
