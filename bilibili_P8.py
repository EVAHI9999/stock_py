#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

# ----------P8 7_将str转换成datetime，使用while循环----------

import requests
#第一个datetime是"包",第二个datetime是"类"，后面的time、timedelta也是类或者子类
from datetime import datetime, time, timedelta
#parser是一个解析器
from dateutil import parser


# ----------list和tuple的区别----------

#list的内容可以是int，也可以是string
list1 = [1, 2, 3]  #list1的内容是int
list2 = ["use", 'python', 'to', 'trade', 'A', 'stock'] #list2的内容是string
#list的内容是可以修改的
print(list1)
list1[1] = 20
print(list1)
print(list2)
list2[4] = 'H'
print(list2)

#tuple的内容是不能修改的
page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
stock_info = page.text
mt_info = stock_info.split(",")
last = float(mt_info[3])
trade_datetime = mt_info[30] + ' ' + mt_info[31]
#因为tick包含收盘价和收盘时间，这些信息会传来传去，我们又不想修改这些信息，因此，打包成tuple类型的tick
tick = (last, trade_datetime)
print(tick)
#tick[0] = 100 #这个语句会报错TypeError
#tick的内容不可以修改，但是可以重新给tick赋值，也即是说，tick是可以整体修改的
tick = 1
print(tick)

# ----------int和float的区别----------

# int -> 整数，float -> 带小数点的
# 以下情况我们可能需要int类型的数据,如order1（第一单）、order（第二单）、order3（第三单）……
order_number = 1
order1 = 'order' + str(order_number)
print(order_number)
print(order1)
order_number = order_number + 1
order2 = 'order' + str(order_number)
print(order_number)
print(order2)
#以下情况我们可能需要float
# 1、价格的计算
# 2、收益的计算

# ----------将string转换成datetime格式----------

#调用datetime里面的today()函数，返回今天的日期和时间
print(datetime.today())
#返回今天的时间，不包括日期
print(datetime.today().time())
#生成一个时间10:00:00
print(time(10))
#时间是可以用来比较的
print(datetime.today().time() > time(10))
#返回今天的日期，不包括时间
print(datetime.today().date())
#以下语句会报错,因为前者包含日期，后者不包含日期，不能直接比较
#print(datetime.today() > time(10))

#将trade_datetime的类型(Type)由string解析(转换成)datetime,解析可以理解为转换数据结构
dt = parser.parse(trade_datetime)
#dt的内容还是日期+时间，type从string变成了datetime
print(dt)
#解析成datetime后，就可以使用其date()了
print(dt.date())
#解析成datetime后，就可以使用其time()了
print(dt.time())
#解析成datetime后，就可以比较时间了
print(dt.time() < time(23))


#----------如何跳出while循环----------
i = 1
while i < 5:
    print('i is: ', i)
    i +=1  #等价于 i = i + 1
print("job done.")


# ----------在交易过程中用while循环----------

# ----------有关函数getTick()的说明，详见bilibili_P7.py
def getTick():  
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
    stock_info = page.text
    mt_info = stock_info.split(",")
    last = float(mt_info[3])
    trade_datetime = mt_info[30] + ' ' + mt_info[31]
    tick = (last, trade_datetime)   
    return tick


# 用时间来跳出while循环

#设定一个交易时间段，来获取数据

# 初始化交易时间，time(9, 30) mean 9:30, time(9) mean 9:00
print(time(9))
print(time(9, 30))
trade_time = time(9, 30)
# 当交易时间在9:00到15:00之间，就会进入到循环当中，调用getTick()去网页获取数据
while time(9) < trade_time < time(15):
    last_tick = getTick()
    print(last_tick)
    #先解析last_tick[1],再取它的time()
    trade_time = parser.parse(last_tick[1]).time()
    #如果没有sleep,打印结果会不断跳出来，非常消耗内存和cpu
    sleep(3)
#为了检验是否从while循环中出来，写了如下print语句
print('job done.')