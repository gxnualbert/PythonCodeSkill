#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-5快速找出多个字典中的公共键.py
@time: 2017/06/21/7:40
"""
# 实际场景
# 西班牙足球甲级联赛，每轮球员进行统计：
# 第一轮：{"梅西":3,"苏亚列":4,"穆泽马":4,"C罗":5...}
# 第二轮：{"苏亚列":1,"梅西":2,"C罗":2,"内马尔":3...}
# 第三轮：{"托雷管":4,"贝尔":1,"内马尔":2,"苏亚列":3...}
# .......
#
# 根据上述比分结果，统计出前N轮比赛中，每轮比赛都有进球的球员

from random import randint,sample

# 使用sample随机产生球员abcdefg，后面的randint(3,6)是随机生成进球球员的进球数，表示3--6个人进球了
sample('abcdefg',randint(3,6))
print sample('abcdefg',randint(3,6))

# sample('abcdefg',randint(3,6))表示随机生成3--6个球员，每个球员的进球数是1--4个（randint(1,4)）
s1={x: randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2={x: randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3={x: randint(1,4) for x in sample('abcdefg',randint(3,6))}

print s1
print s2
print s3

# 最笨的方法：
res=[]
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print res

# 第二种方法：使用字典的viewkeys 方法
print s1.viewkeys()
print s2.viewkeys()
print s3.viewkeys()

print s1.viewkeys()&s2.viewkeys()&s3.viewkeys()