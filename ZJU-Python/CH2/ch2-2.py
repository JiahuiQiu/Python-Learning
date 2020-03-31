# -*- coding: utf-8 -*-
"""
本题目要求计算下列分段函数f(x)的值：

公式 f(x)=1/x, x!=0; f(x)=0, x=0

输入格式:
输入在一行中给出实数x。

输出格式:
在一行中按“f(x) = result”的格式输出，其中x与result都保留一位小数。

输入样例1:
10
输出样例1:
f(10.0) = 0.1

输入样例2:
0
输出样例2:
f(0.0) = 0.0
"""


x = float(input())
result = 0
if x == 0 :
    result = 0
else:
    result = 1/x

print("f(%.1f) = %.1f"%(x,result))

