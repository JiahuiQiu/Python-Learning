# -*- coding: utf-8 -*-
"""
7-14 求整数段和 
给定两个整数A和B，输出从A到B的所有整数以及这些数的和。

输入格式：
输入在一行中给出2个整数A和B，其中−100≤A≤B≤100，其间以空格分隔。

输出格式：
首先顺序输出从A到B的所有整数，每5个数字占一行，每个数字占5个字符宽度，向右对齐。
最后在一行中按Sum = X的格式输出全部数字的和X。

输入样例：
-3 8 
    
输出样例：
   -3   -2   -1    0    1
    2    3    4    5    6
    7    8
Sum = 30
"""


a, b = map(int, input().split())
sums = 0
count =0
if a in range(-100,b+1) and b in range(a,101):
    for i in range(a, b+1):
        sums += i
        count += 1
        if count % 5 != 0:
            print("%5d"%i, end="")
        else:
            print("%5d"%i, end="\n")
        if i == b and count % 5 != 0:
            print()

print("Sum = %d"%sums)

