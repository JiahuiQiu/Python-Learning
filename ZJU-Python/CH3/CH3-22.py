# -*- coding: utf-8 -*-
"""
判断两个字符串是否为变位词 
如果一个字符串是 另一个字符串的重新排列组合，那么这两个字符串互为变位词。比如，”heart”与”earth”互为变位 词，”Mary”与”arMy”也互为变位词。

输入格式:
第一行输入第一个字符串，第二行输入第二个字符串。

输出格式:
输出“yes”,表示是互换词，输出“no”,表示不是互换词。

输入样例1:
在这里给出一组输入。例如：
Mary
arMy

输出样例1
在这里给出相应的输出。例如：
yes

输入样例2:
在这里给出一组输入。例如：
hello 114
114 hello

输出样例2:
在这里给出相应的输出。例如：
yes

输入样例3:
在这里给出一组输入。例如：
Wellcom
mocllew
   
输出样例3:
在这里给出相应的输出。例如：
no

"""


s1 = input()
s2 = input()
lst2 = list(s2)
flag = True

if len(s1) != len(s2):
    flag = False
else:
    for i in range(len(s1)):
        if s1[i] not in lst2:
           flag = False
if flag == True:
    print('yes')
else:
    print('no')




