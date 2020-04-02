# -*- coding: utf-8 -*-
"""
找最长的字符串 
本题要求编写程序，针对输入的N个字符串，输出其中最长的字符串。

输入格式：
输入第一行给出正整数N；随后N行，每行给出一个长度小于80的非空字符串，
其中不会出现换行符，空格，制表符。

输出格式：
在一行中用以下格式输出最长的字符串：
The longest is: 最长的字符串

如果字符串的长度相同，则输出先输入的字符串。

输入样例：
5
li
wang
zhang
jin
xiang
 
输出样例：
The longest is: zhang
"""


N = int(input())
max = 0
str = ''

for i in range(N):
    str = input()
    if len(str) > max:
        max = len(str)
        long = str
print("The longest is:",long)



