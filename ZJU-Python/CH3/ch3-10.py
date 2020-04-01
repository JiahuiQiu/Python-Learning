# -*- coding: utf-8 -*-
"""
字符串排序 
本题要求编写程序，读入5个字符串，按由小到大的顺序输出。

输入格式：
输入为由空格分隔的5个非空字符串，每个字符串不包括空格、制表符、换行符等空白字符，
长度小于80。

输出格式：
按照以下格式输出排序后的结果：
After sorted:
每行一个字符串


输入样例：
red yellow blue green white

输出样例：
After sorted:
blue
green
red
white
yellow
"""


s1, s2, s3, s4, s5 = input().split(" ")
print("After sorted:")
lst1 = [s1, s2, s3, s4, s5]
lst1.sort()
for i in range(len(lst1)):
    print(lst1[i])


