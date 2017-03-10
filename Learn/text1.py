# -*- coding: utf-8 -*-

import re


def findPart(regex, text, name):
    res = re.findall(regex, text)
    if res:
        print("There are %d %s parts:\n" % (len(res), name))
        for r in res:
            print("\t", r)
        print()

#sample is utf8 by default.
sample='''en: Regular expression is a powerful tool for manipulating text.
zh: 正则表达式是一种很有用的处理文本的工具。
jp: 正規表現は非常に役に立つツールテキストを操作することです。
jp-char: あアいイうウえエおオ
kr:정규 표현식은 매우 유용한 도구 텍스트를 조작하는 것입니다.
puc: 。？！、，；：“ ”‘ ’——……·－·《》〈〉！￥％＆＊＃
'''
#let's look its raw representation under the hood:
print("the raw utf8 string is:\n", repr(sample))
print()

#find the non-ascii chars:
findPart(r"[\x80-\xff]+", sample, "non-ascii")

#convert the utf8 to unicode
sample.encode("utf-8")

#let's look its raw representation under the hood:
print("the raw unicode string is:\n", repr(sample))
print()

#get each language parts:
findPart(u"[\u4e00-\u9fa5]+", sample, "unicode chinese")
findPart(u"[\uac00-\ud7ff]+", sample, "unicode korean")
findPart(u"[\u30a0-\u30ff]+", sample, "unicode japanese katakana")
findPart(u"[\u3040-\u309f]+", sample, "unicode japanese hiragana")
findPart(u"[\u3000-\u303f\ufb00-\ufffd]+", sample, "unicode cjk Punctuation")