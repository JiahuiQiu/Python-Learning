# -*- coding: utf-8 -*-
"""
字符串字母大小写转换 
本题要求编写程序，对一个以“#”结束的字符串，将其小写字母全部转换成大写字母，
把大写字母全部转换成小写字母，其他字符不变输出。

输入格式：
输入为一个以“#”结束的字符串（不超过30个字符）。

输出格式：
在一行中输出大小写转换后的结果字符串。

输入样例：
Hello World! 123#
    
输出样例：
hELLO wORLD! 123
"""


a = input()
b = ""

for i in range(len(a)-1):
    if 'a'<=a[i]<='z':
        b += a[i].upper()
    elif 'A'<=a[i]<='Z':
        b += a[i].lower()
    elif a[i] == "#":
        b = b + ""
    else:
        b = b + a[i]

print(b)


