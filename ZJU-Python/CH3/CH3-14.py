# -*- coding: utf-8 -*-
"""
统计一行文本的单词个数 (15分)
本题目要求编写程序统计一行字符中单词的个数。所谓“单词”是指连续不含空格的字符串，
各单词之间用空格分隔，空格数可以是多个。

输入格式:
输入给出一行字符。

输出格式:
在一行中输出单词个数。

输入样例:
Let's go to room 209.

输出样例:
5
"""


sentence = input()
lst1 = sentence.split()
count =0
for word in lst1:
    count += 1
print(count)


