# -*- coding: utf-8 -*-
"""
比较大小 
本题要求将输入的任意3个整数从小到大输出。

输入格式:
输入在一行中给出3个整数，其间以空格分隔。

输出格式:
在一行中将3个整数从小到大输出，其间以“->”相连。

输入样例:
4 2 8

输出样例:
2->4->8
"""


a, b, c = map(int, input().split())
lis = [a, b, c]
for i in range(len(lis)-1):
    for j in range(len(lis)-1-i):
        if lis[j] > lis[j+1]:
            lis[j], lis[j+1] = lis[j+1], lis[j]

print('%d->%d->%d'%(lis[0],lis[1],lis[2]))