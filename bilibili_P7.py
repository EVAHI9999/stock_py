#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

# ----------从网页提取所需的报价信息----------

# F9:逐行运行
# requests是用来解析网页的
import requests
from time import sleep

# def是定义函数/功能
# 函数getTick()的作用：去sina获取最新的tick，tick包括最新成交价和成交时间
def getTick():
    #用get去建立链接，page的type是models.Response,page的内容是Response object,里面没有信息
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
    #把page的text给get出来，转移text信息
    #网页内容是股票的信息，取名stock_info，其类型是string，长度为254
    stock_info = page.text
    
    # #string相关知识
    # string1 = "abc"
    # string2 = "use python to trade A stock"
    # #用空格“切”string2，并放在容器list1中，list1的大小是6
    # list1 = string2.split(' ')
    # #取list1的内容
    # print(list1[0])
    # print(list1[1])
    # print(list1[2])
    # print(list1[3])
    # print(list1[4])
    # print(list1[5])
    # #string不能和int相加
    
    #用逗号切割类型为string的stock_info，生成一个类型为list的mt_info.mt表示茅台
    mt_info = stock_info.split(",")
    
    #mt_info的数据很多，我们只去其中的开盘价、最高价、最低价、收盘价、日期、时间等信息
    #mt_info[0] 股票代码及名称
    #mt_info[1] 开盘价
    #mt_info[2] 昨天收盘价
    #mt_info[3] 最新成交价
    #mt_info[4] 最高价
    #mt_info[5] 最低价
    #mt_info[30] 日期
    #mt_info[31] 时间，收盘时间为15:00:01


    #最新成交价，因为mt_info[3]的类型是string，所以需要改成float，才能进行后续的计算
    last = float(mt_info[3])
    #成交时间
    trade_datetime = mt_info[30] + ' ' + mt_info[31]

    #将最新成交价和成交时间封装到容器tick中，tick的type为tuple
    tick = (last, trade_datetime)
    # print(tick)
    # print(tick[0])
    # print(tick[1])
    
    return tick

#用一个循环不断去获取数据
while True:
    last_tick = getTick()
    print(last_tick)

    #wait for 3 second
    sleep(3)

# #接下来的一部分内容及代码是在P8视频里讲到了
# #设定一个交易时间段，来获取数据
# from datetime import datetime, time
# from dateutil import parser

# #time(9, 30) mean 9:30, time(9) mean 9:00
# trade_time = time(9, 30)
# while time(9) < trade_time < time(15):
#     last_tick = getTick()
#     print(last_tick)
#     trade_time = parser.parse(last_tick[1]).time()
#     sleep(3)
# print('job done.')