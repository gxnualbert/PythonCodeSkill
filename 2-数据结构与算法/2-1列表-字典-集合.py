#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-4根据字典值大小对字典排序.py
@time: 2017/06/20/20:33
"""
# 1、过滤列表中的负数
# 2、筛选出字典中值高于90的项
# 3、筛选出集合中能被3整除的元素

from random import randint
from timeit import timeit as timeit

# 1、过滤列表中的负数
# 在-10 和 10 之间生成10个随机数
data=[randint(-10,10) for _ in xrange(10)]
print data
# 第一种方式
# lambda 匿名函数，需要一个入参，后面加一个布尔值，如果为真，就返回出来。在这里，x就是上面的列表中的元素
a=filter(lambda x:x>=0,data)
print a

# 第二种方式：使用列表解析
# for x in data 遍历data中的每个元素，然后通过if x>=0，如果为真，就返回给第一个x
b=[x for x in data if x>=0]
print b
# 使用timeit的时候出问题，后面有空再看看
# t1=timeit.Timer('filter(lambda x:x>=0,data)')
# print t1.timeit()
# print timeit('filter(lambda x:x>=0,data)')

# 2、筛选出字典中值高于90的项
#  {x for x in xrange(1,21)} 随机生成1-20 个数，作为学号，
# 其中randint(60,100)为60--100之间的随机数，作为分数。因此，该字典d
# 的意思就是字典的键是学号，字典的值是分数
d={x:randint(60,100) for x in xrange(1,21)}
print d
# for x in d,这种只能迭代出字典的键，要迭代字典的键值，需要用for k,v in d.iteritems()
# {k:v for k,v in d.iteritems() if v >90} 这句话的意思就是，迭代字典d的键值，如果v的值>90，那么将返回键值对k,v
dict1={k:v for k,v in d.iteritems() if v >90}
print dict1

# 3、筛选出集合中能被3整除的元素

# 将上面的列表data编程一个集合
# s=set(data)
# print set(data)
# set([1, 6, 8, -10, -9, -8, -6, -1]) 这里没有转成功，但是web ide可以转成功，原因未知（主要原因是视频中用的是py3)
# 所以先用写死的集合代替一下
s={-10,-9,-8,-7,-1,4,5,9}
s1={x for x in s if x %3==0}
print s1

# 什么是列表呢？我觉得列表就是我们日常生活中经常见到的清单。比如，统计过去一周我们买过的东西，把这些东西列出来，
# 就是清单。由于我们买一种东西可能不止一次，所以清单中是允许有重复项的。如果我们扩大清单的范围，统计我们过去一周
# 所有的花费情况，那么这也是一个清单，但这个清单里会有类别不同的项，比如我们买东西是一种花费，交水电费也是一种花费，
# 这些项的类型是可以使不同的。python的列表个跟清单的道理是一样的，特点就是：可重复，类型可不同。类型不同也是跟数组
# 最本质的区别了。python里的列表用“[]”表示

# 元组和列表在结构上没有什么区别，唯一的差异在于元组是只读的，不能修改。元组用“()”表示

# 集合就是我们数学学的集合，没有什么特殊的定义。集合最好的应用是去重。集合没有特殊的表示方法，而是通过一个
# set函数转换成集合

# 字典存储键值对数据 字典最大的价值是查询，通过键，查找值