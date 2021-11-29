#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

# ----------bar的聚合与更新----------

import requests
from time import sleep
from datetime import datetime, time
from dateutil import parser

def getTick():
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
    stock_info = page.text
    mt_info = stock_info.split(",")
    last = float(mt_info[3])
    trade_datetime = mt_info[30] + ' ' + mt_info[31]
    tick = (last, trade_datetime)   
    return tick

def get_history_data_from_local_machine():
    #some code here
    #dt = ******
    return dt, open_, high_, low_, close_, volume_

def bar_generator(tick, Dt, Open, High, Low, Close, Volume):
    # 交易想法
    # 买入：价格低于MA20 * 0.95
    # 卖出：价格高于MA20 * 1.05
    # 我们需要做：
    # 1、更新5分钟K线的ma20
    # 2、比较价格与ma20 * 0.95及ma20 * 1.05的关系，确定买或卖或忽略
    
    # ？？？？？？？？？？下一句print为什么会语法错误？？？？？？？？？？
    print(datetime(2020, 11, 27. 14, 55))
    Dt = [datetime(2020, 11, 27. 14, 55),
          datetime(2020, 11, 27. 14, 50),
          datetime(2020, 11, 27. 14, 45)]
    print(Dt)
    Open = [45.79, 45.66, 45.72]
    print(Open)
    Hign = []
    Low = []
    Close = []
    
    #tick[0]为交易价格，tick[1]为交易时间，视频作者将tick[0]说成交易时间了
    print(tick[0])
    print(tick[1])
    #tick[1]的type为string，需要先改type为datetime才可以用minute
    print(parser.parse(tick[1]).minute)
    
    last_bar_start_minute = None
    # 如果满足条件，创建一个新的bar
    if tick[0].minute % 5 == 0 and \
        tick[0].minute != last_bar_start_minute:
        #创建一个新的蜡烛图
        last_bar_start_minute = tick[0].minute
        Open.insert(0, tick[1])
        High.insert(0, tick[1])
        Low.insert(0, tick[1])
        Close.insert(0, tick[1])
        #用Dt的第一个元素，即Dt[0]存放最新的日期
        Dt.insert(0, tick[0])
        #计算一个新的MA20
   
    # 否则，更新当前bar    
    else:
        #更新蜡烛图
        High[0] = max(High[0], tick[1])
        Low[0] = min(Low[0], tick[1])
        Close[0] = tick[1]
        Dt[0] = tick[0]
        
    return Dt, Open, High, Low, Close, Volume

def buy():
    pass
def sell():
    pass

def strategy(Dt, Open, High, Low, Close, Volume):    
    ma20 = Close[:19].sum()/20
    
    if new bar is created:
        sum_ = 0
        for item in Close[1:21]:
            sum_ = sum_ + item
        ma20 = sum_/20
    
    #接下来是比较
    if Close[0] < 0.95 * ma20:
        buy()
    elif Close[0] > ma20 * 1.05:
        if I have long position:    
            sell()
        else:
            pass
    else:
        # Close[0] in between 0.95*ma20 and 1.05*ma20, do nothing
        pass
    compare

class platform(object):
    pass

#----------------------------------------------------------------------------
#time(9, 30) mean 9:30, time(9) mean 9:00
Dt_, Open_, High_, Low_, Close_, Volume_ = \
get_history_data_from_local_machine
trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    Dt, Open, High, Low, Close, Volume = \
    bar_generator(last_tick, Dt, Open, High, Low, Close, Volume)
    print(last_tick)
    strategy(Dt, Open, High, Low, Close, Volume)
    # trade_time = parser.parse(last_tick[1]).time()
    sleep(3)
print('job done.')