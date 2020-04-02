# -*- coding: utf-8 -*-
"""
逆序的三位数 
程序每次读入一个正3位数，然后输出按位逆序的数字。
注意：当输入的数字含有结尾的0时，输出不应带有前导的0。比如输入700，输出应该是7。

输入格式：
每个测试是一个3位的正整数。

输出格式：
输出按位逆序的数。

输入样例：
123
 
输出样例：
321
"""


Num = int(input())
hundreds_digit = Num//100
digit = Num%10
tens_digit = (Num%100)//10
reverseNum = digit*100 + tens_digit*10 + hundreds_digit
print(reverseNum)



