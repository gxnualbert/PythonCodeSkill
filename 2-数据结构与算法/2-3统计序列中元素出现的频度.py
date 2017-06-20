#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-4根据字典值大小对字典排序.py
@time: 2017/06/20/21:30
"""
# 问题1：某随机序列[4, 8, 7, 6, 0, -4, 7, 9, -1, -10,8,....]中，找到出现次数最高的3个元素
# 他们出现的次数是多少
# 问题2：对某英文文章，进行词频统计，找到出现次数最高的10个单词，他们出现次数是多少


# 问题1解决方案：将序列传入Counter的构造器中，得到Counter对象是元素频度的字典，most_common方法得到频度
# 最高的n个元素的列表
from random import randint
from collections import Counter
import re

data=[randint(-10,10) for _ in xrange(30)]
print data
c2=Counter(data)
print c2
print c2.most_common(3)



# 问题2解决方案
# 首先读入一篇文章，然后通过正则表达式分割单词，然后再通过Counter这个函数进行统计
txt=open('English.txt').read()
a=re.split('\W+',txt) #[\w+]表示匹配数字、字母、下划线和加号本身字符；
c3=Counter(a)
c3.most_common()
print c3
print c3.most_common(10)