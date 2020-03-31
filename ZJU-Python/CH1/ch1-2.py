# -*- coding: utf-8 -*-
"""
在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值
"""

a, b, c = map(int,input().split())
print(b*b-4*a*c)