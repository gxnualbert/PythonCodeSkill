#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-4根据字典值大小对字典排序.py
@time: 2017/06/20/21:15
"""
# 如何为元组中的每个元素命名，提高程序可读性？
#
# 学生信息系统中数据为固定格式：
# （名字，年龄，性别，邮箱地址，...）
# 学生数量很大，为了减小存储开销，对每个学生信息用元组表示：
# student1=('Jim',16,'male','Jim93@gmail.com')
# ('Lilei',17,'male','lilei@gmail.com')
# ('Lucy',16,'male','Lucy@wesoft.com')
# ......
# 访问这些学生数据的时候，我们将使用索引来访问，大量索引降低了程序的可读性。例如，访问姓名：
# student1[0],访问年龄student1[1],

# 解决方案
# 第一种：定义类似其他语言的枚举类型，也就是定义一系列数值常量
# 第二种：使用标准库中collections.nametuple替代内置tuple

# 方案一：
NAME,AGE,SEX,EMAIL=xrange(4)# 表示将随机生成的0,1,2,3分别赋值给NAME,AGE,SEX,EMAIL
student=('Jim',16,'male','Jim93@gmail.com')
# 当我们访问名字时，只需student[NAME], 而不用student[0]，你单单从0看不出该变量代表什么
print student[NAME]

# 方案二：
print '方案二'
from collections import namedtuple
# Student=namedtuple('Student',['name','age','sex','email']) 在namedtuple中，第一个参数Student 表示你自己为
# 新创建的类起一个名字，可以随便写，这里用Student。后面的['name','age','sex','email']表示索引对应的名字
student=namedtuple('Student',['name','age','sex','email'])

s=student('Jim',16,'male','Jim93@gmail.com')
print s
print s.email