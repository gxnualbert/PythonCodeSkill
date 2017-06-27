#!usr/bin/env python 2.7.12
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 利用生成器函数实现可迭代对象.py
@time: 2017/06/27/20:19
"""
# 先理解一个概念：什么是素数
# 素数的定义
# 在大于1的整数中，只能被1和这个数本身整除的数，如2、3、5、7、11。也叫质数

# 实现一个可迭代对象的类，它能迭代出给定范围内所有素数：
#
#
# 解决方案：将该类的__iter__方法实现生成器函数，每次yield返回一个素数


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in xrange(2, k):
            if k % 2 == 0:
                return False

        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k


for x in PrimeNumbers(1, 100):
    print x
