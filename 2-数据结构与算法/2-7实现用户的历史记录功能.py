#!usr/bin/env python 2.7.12
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: 2-7实现用户的历史记录功能.py
@time: 2017/06/26/20:57
# """
# 很多的应用程序都有浏览用户的历史记录的功能，例如：
# 浏览器可以产看最近访问过的网页
# 视频播放器可以产看最近播放过的视频文件
# shell可以查看用户输入过的命令
# ......
#
# 现在我们制作一个简单的猜数字的小游戏，添加历史记录功能，显示用户最近猜过的数字，如何实现？

# 解决办法：使用容量为n的队列存储历史记录
# 使用标准库collections中的deque，它是一个双端循环队列
# 程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入

from random import randint
from collections import deque
import pickle #由于deque只存在内存中，所以需要将python对象转化为文件保存在磁盘上


n=randint(0,100)#产生一个0--100的随机数
history=deque([],5)#初始化队列，队列中只能储存5个值
def guess(k):
    if k==n:
        print 'right'
        return True
    if k<n:
        print '%s is less than n'%k
    else:
        print '%s is bigger than n' %k
    return False

while(True):
    line=raw_input('please input a number: ')
    #  isdigit() 方法检测字符串是否只由数字组成。
    if line.isdigit():
        k=int(line)
        history.append(k)
        if guess(k):
            break
    elif line=='history' or line=='h':
        print list(history)

pickle.dump(history,open('history.txt','w'))#将对象存入history txt文件中

q2=pickle.load(open('history.txt'))
print 'q2 is:',q2