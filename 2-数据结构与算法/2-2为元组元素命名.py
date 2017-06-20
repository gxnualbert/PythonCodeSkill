# -*- coding:utf-8 -*-
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
# student1[0],访问年龄student1[0],

# 解决方案
# 第一种：定义类似其他语言的枚举类型，也就是定义一系列数值常量
# 第二种：使用标准库中collections.nametuple替代内置tuple

