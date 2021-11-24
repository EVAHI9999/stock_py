#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

import requests
#第一个datetime是"包",第二个datetime是"类"，后面的time、timedelta也是类或者子类
from datetime import datetime, time, timedelta
#parser是一个解析器
from dateutil import parser


#list和tuple的区别

#list的内容可以是int
list1 = [1, 2, 3]
#list的内容可以是string
list2 = ["use", 'python', 'to', 'trade', 'A', 'stock']
#list的内容是可以修改的
list1[1] = 20
list2[4] = 'H'

#tuple的内容是不能修改的
page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
stock_info = page.text
mt_info = stock_info.split(",")
last = float(mt_info[3])
trade_datetime = mt_info[30] + ' ' + mt_info[31]
tick = (last, trade_datetime)
#tick[0] = 100，这个语句会报错TypeError

#int和float的区别

#以下情况我们可能需要int类型的数据
order_number = 1
order1 = 'order' + str(order_number)
order_number = order_number + 1
order2 = 'order' + str(order_number)

#将string转换成datetime格式

#直接调用datetime里面的today()函数，就可以返回今天的日期和时间
print(datetime.today())
#直接返回今天的时间，不包括日期
print(datetime.today().time())
#时间是可以用来比较的
print(datetime.today().time() > time(10))
#直接返回今天的日期，不包括时间
print(datetime.today().date())
#以下语句会报错,因为前者包含日期，后者不包含日期，不能直接比较
#print(datetime.today() > time(10))

#将trade_datetime的类型(Type)由string解析(转换成)datetime
dt = parser.parse(trade_datetime)
#解析成datetime后，就可以使用其date()了
print(dt.date())
#解析成datetime后，就可以使用其time()了
print(dt.time())
#解析成datetime后，就可以比较时间了
print(dt.time() < time(23))


#如何跳出while循环
i = 1
while i < 5:
    print('i is: ', i)
    i +=1  #等价于 i = i + 1
print("job done.")
