#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

# ----------P9 8_设计一个简单的策略----------

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

#设计一个朴素的交易策略
def strategy(tick):
    # 交易想法
    # 买入：价格低于MA20 * 0.95
    # 卖出：价格高于MA20 * 1.05
    # 我们需要做：
    # 1、更新5分钟K线的ma20
    # 2、比较价格与ma20 * 0.95及ma20 * 1.05的关系，确定买或卖或忽略
    pass