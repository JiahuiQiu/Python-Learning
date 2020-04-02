# -*- coding: utf-8 -*-
"""
字符串替换 
本题要求编写程序，将给定字符串中的大写英文字母按以下对应规则替换：

原字母	对应字母
A	Z
B	Y
C	X
D	W
…	…
X	C
Y	B
Z	A
输入格式：
输入在一行中给出一个不超过80个字符、并以回车结束的字符串。

输出格式：
输出在一行中给出替换完成后的字符串。

输入样例：
Only the 11 CAPItaL LeTtERS are replaced.
 
输出样例：
Lnly the 11 XZKRtaO OeGtVIH are replaced.

"""

str_in = input()
str_out = ''

for i in range(len(str_in)):
    if 'A' <= str_in[i] <= 'Z':
        str_out += chr(ord('A')+ord('Z')-ord(str_in[i]))
    else:
        str_out += str_in[i]
print(str_out)

