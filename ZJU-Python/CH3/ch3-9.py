# -*- coding: utf-8 -*-
"""
统计大写辅音字母
英文辅音字母是除A、E、I、O、U以外的字母。本题要求编写程序，
统计给定字符串中大写辅音字母的个数。

输入格式：
输入在一行中给出一个不超过80个字符、并以回车结束的字符串。
输出格式：
输出在一行中给出字符串中大写辅音字母的个数。

输入样例：
HELLO World!
输出样例：
4
"""


str1 = input()
str2 = 'AEIOU'
count = 0

for i in str1:
    if i == i.upper() and i.upper() >= 'A' and i.upper() <= 'Z':
        if i not in str2:
            count += 1
print(count)
      


