# -*- coding: utf-8 -*-
"""
猴子吃桃问题
"""

n = 1
for i in range(5, 0, -1):
    n = (n+1) << 1
print(n)

