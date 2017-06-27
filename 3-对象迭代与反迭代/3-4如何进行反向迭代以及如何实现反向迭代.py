#!usr/bin/env python 2.7.12
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 3-4如何进行反向迭代以及如何实现反向迭代.py
@time: 2017/06/27/20:38
"""

# 实际案例：
# 实现一个连续浮点数发生器FloatRange(和xrange 类似)，根据给定范围（ start, end,）和步进值（step）产生一系列连续浮点数，
# 如迭代FloatRange（3.0,4.0,0.2）可产生序列：
#
# 正向:3.0->3.2->3.4->3.6->3.8->4.0
# 反向：4.0->3.8->3.6->3.4->3.2->3.0
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

for x in reversed(FloatRange(3.0,4.0,0.2)):
    print x

for x in (FloatRange(3.0,4.0,0.2)):
    print x
