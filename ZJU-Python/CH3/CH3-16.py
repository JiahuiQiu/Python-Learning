# -*- coding: utf-8 -*-
"""
删除字符 
输入一个字符串 str，再输入要删除字符 c，大小写不区分，
将字符串 str 中出现的所有字符 c 删除。

输入格式:
在第一行中输入一行字符 在第二行输入待删除的字符

输出格式:
在一行中输出删除后的字符串

输入样例:
在这里给出一组输入。例如：
        Bee
   E

输出样例:
在这里给出相应的输出。例如：
result: B

"""


str = input().strip()
c = input().strip()
print("result:", str.replace(c.upper(), '').replace(c.lower(), ''))




