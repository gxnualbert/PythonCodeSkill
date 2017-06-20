#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-4根据字典值大小对字典排序.py
@time: 2017/06/20/22:13
"""

# 案例：根据字典中值的大小，对字典中的项进行排序
# 某班英语成绩一字典的形式存储为：
# {'LiLei':79,'Jim':88,'Lucy':92.....}
# 根据成绩高低，计算学生排名
#
# 解决方案：
# 使用内置函数sorted
#
# 1.利用zip将字典数据转化为元组，也就是将字典的每个键值对打包成一个元组，然后再通过元组进行比较
# 2.传递sorted函数的key参数

from random import randint
d={x:randint(60,100) for x in 'xyzabc'}#使用xyzabc每一个字母代表一个学生，总共有6个学生。学生的分数由randint(60,100)随机产生
print d
# 如下所示，使用sorted对字典进行排序，只是对字典的键进行排序，并没有对值进行排序
print sorted(d)

# 使用zip函数后，字典的键值对变成一个元组[(86, 'a'), (90, 'c'), (70, 'b'), (83, 'y'), (98, 'x'), (66, 'z')]
zip(d.values(),d.keys())
print zip(d.values(),d.keys())
# 然后再用sorted进行排序
sorted(zip(d.values(),d.keys()))
print sorted(zip(d.values(),d.keys()))

# 第二种方法：
# 通过d.items() 可以直接得出字典的元组形式，如：
# 但是该形式中，第一个是键，并不是值，不能进行排序
# 使用sorted函数，然后制定进行排序的键为字典中的值，即可实现

d.items()
print d.items()
# 每次迭代d.items()，把其中的某一个项（例如('y', 88)）放入到lambda函数中，x[0]为学生名y,x[1]为分数88
# 然后制定sorted中，排序的key为每一个项中的第二个值x[1]（第一个是x[0]）
sorted(d.items(),key=lambda x:x[1])
print sorted(d.items(),key=lambda x:x[1])