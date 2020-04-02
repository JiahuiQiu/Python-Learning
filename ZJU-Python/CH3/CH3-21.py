# -*- coding: utf-8 -*-
"""
输出大写英文字母 
本题要求编写程序，顺序输出给定字符串中所出现过的大写英文字母，每个字母只输出一遍；
若无大写英文字母则输出“Not Found”。

输入格式：
输入为一个以回车结束的字符串（少于80个字符）。

输出格式：
按照输入的顺序在一行中输出所出现过的大写英文字母，每个字母只输出一遍。
若无大写英文字母则输出“Not Found”。

输入样例1：
FONTNAME and FILENAME

输出样例1：
FONTAMEIL
    
输入样例2：
fontname and filrname

输出样例2：
Not Found
"""


s = input()
list = []
for i in range(len(s)):
    if 'A'<=s[i]<='Z' and s[i] not in list:
        list.append(s[i])
if len(list)==0:
    print("Not Found")
else:
    print(''.join(list))



