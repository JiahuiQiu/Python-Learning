# -*- coding: utf-8 -*-
"""
求整数的位数及各位数字之和 
对于给定的正整数N，求它的位数及其各位数字之和。

输入格式：
输入在一行中给出一个不超过10^​9的正整数N。

输出格式：
在一行中输出N的位数及其各位数字之和，中间用一个空格隔开。

输入样例：
321 
输出样例：
3 6
"""


num = input()
lst1 = list(num)
sum =0
cnt = len(lst1)
for i in range(cnt):
    sum += int(lst1[i])

print(cnt, sum)
   
 
    


