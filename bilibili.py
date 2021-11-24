#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

#requests是用来解析网页的
import requests
from time import sleep

def getTick():
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
    stock_info = page.text
    mt_info = stock_info.split(",")

    last = float(mt_info[3])
    trade_datetime = mt_info[30] + ' ' + mt_info[31]

    tick = (last, trade_datetime)
    
    return tick

while True:
    last_tick = getTick()
    print(last_tick)

    #wait for 3 second
    sleep(3)

