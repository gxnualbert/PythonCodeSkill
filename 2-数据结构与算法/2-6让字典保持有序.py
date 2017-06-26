#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-6让字典保持有序.py
@time: 2017/06/26/20:17
"""

# 某编程竞赛系统，对编程的参赛选手的解题时间进行计时，选手完成题目后，把该选手的解题用时记录到字典中，以便赛后选手查询成绩
# （答题用时越短，成绩越优）
# {"LiLei":(2,43),"HanMeiMei":(5,52),"Jim":(1,39)......}
# "HanMeiMei":(5,52)表示学生HanMeiMei，获得第5名，用时52分
# 比赛结束后，需按排名顺序依次打印选手成绩，如何实现？？

# 解决方案：使用collections.OrderedDict ,以OrderedDict代替内置字典Dict，依次将选手成绩存入

from collections import OrderedDict
from time import time
from random import randint

d = OrderedDict()
start = time()
players = list('ABCDEFGH')

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start
    d[p] = (i + 1, end - start)

for k in d:
    print k,d[k]