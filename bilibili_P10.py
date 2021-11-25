#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

#requests是用来解析网页的
import requests
from time import sleep

def getTick():
    #用get去建立链接，里面没有信息
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
    #转移text信息，stock_info的类型是string
    stock_info = page.text
    #用逗号切割类型为string的stock_info，生成一个类型为list的mt_info
    mt_info = stock_info.split(",")
    
    #mt_info[0] 股票代码及名称
    #mt_info[1] 开盘价
    #mt_info[2] 昨天收盘价
    #mt_info[3] 实时价
    #mt_info[4] 最高价
    #mt_info[5] 最低价
    #mt_info[30] 日期
    #mt_info[31] 时间，收盘时间为15:00:01

    #选取最新成交价，因为mt_info[3]的类型是string，所以需要改成float
    last = float(mt_info[3])
    #选取成交时间
    trade_datetime = mt_info[30] + ' ' + mt_info[31]

    #将所选数据组成一个tuple
    tick = (last, trade_datetime)
    
    return tick

#用一个循环不断去获取数据
# while True:
#     last_tick = getTick()
#     print(last_tick)

#     #wait for 3 second
#     sleep(3)

#接下来的一部分内容及代码是在P8视频里讲到了
#设定一个交易时间段，来获取数据
from datetime import datetime, time
from dateutil import parser

#time(9, 30) mean 9:30, time(9) mean 9:00
trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    print(last_tick)
    strategy(last_tick)
    trade_time = parser.parse(last_tick[1]).time()
    sleep(3)
print('job done.')

#设计一个朴素的交易策略
def strategy(tick, Dt, Open, High, Low, Close):
    #买入：价格低于MA20 * 0.95
    #卖出：价格高于MA20 * 1.05
    #1、更新5分钟K线的ma20
    #2、判断价格与ma20 * 0.95及ma20 * 1.05的关系，确定买或卖或通过
    Dt = [datetime(2020, 11, 27. 14, 55),
          datetime(2020, 11, 27. 14, 50),
          datetime(2020, 11, 27. 14, 45)]
    Open = [45.79, 45.66, 45.72]
    Hign = []
    Low = []
    Close = []
    
    last_bar_start_minute = None
    if tick[0].minute % 5 == 0 and \
        tick[0].minute != last_bar_start_minute:
        #创建一个新的蜡烛图
        last_bar_start_minute = tick[0].minute
        Open.insert(0, tick[1])
        High.insert(0, tick[1])
        Low.insert(0, tick[1])
        Close.insert(0, tick[1])
        Dt.insert(0, tick[0])
        #计算一个新的MA20
        ma20 = Close[:19].sum()/20
    else:
        #更新蜡烛图
        High[0] = max(High[0], tick[1])
        Low[0] = min(Low[0], tick[1])
        Close[0] = tick[1]
        Dt[0] = tick[0]
    pass