#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

# ----------P10 9_bar的聚合与更新----------

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

trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    print(last_tick)
    strategy(last_tick)
    trade_time = parser.parse(last_tick[1]).time()
    sleep(3)
print('job done.')

def strategy(tick, Dt, Open, High, Low, Close, Volume):
    # 交易想法
    # 买入：价格低于MA20 * 0.95
    # 卖出：价格高于MA20 * 1.05
    # 我们需要做：
    # 1、更新5分钟K线，并计算5分钟的ma20
    # 2、比较价格与ma20 * 0.95及ma20 * 1.05的关系，确定买或卖或忽略
    
    # 用datetime创建一个时间，包含：日期+时+分
    dt = datetime(2020, 11, 27, 14, 55)
    print(dt)
    print(dt.minute)
    
    # Dt、Open、High、Low、Close的历史数据
    Dt = [datetime(2020, 11, 27, 14, 55),
          datetime(2020, 11, 27, 14, 50),
          datetime(2020, 11, 27, 14, 45)]
    print(Dt)
    Open = [45.79, 45.66, 45.72]
    print(Open)
    High = []
    Low = []
    Close = []
    
    #tick[0]为交易价格，tick[1]为交易时间，视频作者将tick[0]说成交易时间了
    print(tick[0])
    print(tick[1])
    #tick[1]的type为string，需要先改type为datetime才可以用minute
    print(parser.parse(tick[1]).minute)
    
    # 初始化最新bar的分钟
    last_bar_start_minute = None
    # 如果满足条件，创建一个新的bar
    # 条件1：交易时间的分钟÷5的余数为0。有了这个条件，就会在9:35、9:40、9:45……产生一个新的bar
    # 条件2：交易时间的分钟不等于前一个交易时间的分钟。有了这个条件，就不会在9:35:03、9:35:06、9:35:09……产生新的bar
    # % 取余
    # 5 表示5分钟更新一个bar，即5分钟K，也可以是10、20、30……。但是60可以吗？
    if tick[0].minute % 5 == 0 and \
        tick[0].minute != last_bar_start_minute:

        # 更新bar的分钟
        last_bar_start_minute = tick[0].minute
        
        #创建一个新的蜡烛图
        # 新bar的Open、High、Low、Close都等于tick[1]
        #用Open的第一个元素，即Open[0]存放最新的开盘价
        Open.insert(0, tick[1])
        #用High的第一个元素，即High[0]存放最新的最高价
        High.insert(0, tick[1])
        #用Low的第一个元素，即Low[0]存放最新的最低价
        Low.insert(0, tick[1])
        #用Close的第一个元素，即Close[0]存放最新的收盘价
        Close.insert(0, tick[1])
        #用Dt的第一个元素，即Dt[0]存放最新的日期
        Dt.insert(0, tick[0])
        #计算一个新的MA20，因为ma20只需要计算一次，因此可在创建新bar时计算
        ma20 = Close[:19].sum()/20
   
    # 否则，更新当前bar    
    else:
        #更新蜡烛图
        
        # 1、Open不需要update
        # 2、High取High[0]和tick[1]的最高价
        High[0] = max(High[0], tick[1])
        # 3、Low取Low[0]和tick[1]的最低价
        Low[0] = min(Low[0], tick[1])
        # 4、Close及时更新，取tick[1]
        Close[0] = tick[1]
        # 5、Dt及时更新，取tick[0]
        Dt[0] = tick[0]
        
    return Dt, Open, High, Low, Close, Volume

