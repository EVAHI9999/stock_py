#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

# ----------P13 11.2_用“类”改造代码----------
# 用“类”改造代码的目标：避开参数频繁的传递
# 面向过程，需要return，面向对象，不需要return

import requests
from time import sleep
from datetime import datetime, time
from dateutil import parser

# 函数 function
# 参数 variable
# 类 class
    # variable -> attribute， 属性
    # function -> method， 方法

def getTick():
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
    stock_info = page.text
    mt_info = stock_info.split(",")
    last = float(mt_info[3])
    trade_datetime = mt_info[30] + ' ' + mt_info[31]
    tick = (last, trade_datetime)   
    return tick

class AstockTrading(object):
    def __init__(self):
        self.Dt = None
        self.Open = None
        self.High = None
        self.Low = None
        self.Close = None
        self.Volume = None
        
    #更新历史数据
    def get_history_data_from_local_machine(self):
        self.Open = [1, 2, 3]
        self.High = [2, 3, 4]
        
    # 面向过程 -> 面向对象
    # 函数的功能bar_generator：传递tick数据进来，更新bar
    def bar_generator(self, tick):
        # 交易想法
        # 买入：价格低于MA20 * 0.95
        # 卖出：价格高于MA20 * 1.05
        # 我们需要做：
        # 1、更新5分钟K线，并计算5分钟的ma20
        # 2、比较价格与ma20 * 0.95及ma20 * 1.05的关系，确定买或卖或忽略
        
        # 用datetime创建一个时间，包含：日期+时+分
        # dt = datetime(2020, 11, 27, 14, 55)
        # print(dt)
        # print(dt.minute)
        
        # # Dt、Open、High、Low、Close的历史数据
        # Dt = [datetime(2020, 11, 27, 14, 55),
        #       datetime(2020, 11, 27, 14, 50),
        #       datetime(2020, 11, 27, 14, 45)]
        # print(Dt)
        # Open = [45.79, 45.66, 45.72]
        # print(Open)
        # High = []
        # Low = []
        # Close = []
       
       
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
            #面向对象之后，需要把Open修改成self.Open
            self.Open.insert(0, tick[1])
            self.High.insert(0, tick[1])
            self.Low.insert(0, tick[1])
            self.Close.insert(0, tick[1])
            self.Dt.insert(0, tick[0])
             
        # 否则，更新当前bar    
        else:
            #更新蜡烛图
            
            # 1、Open不需要update
            self.High[0] = max(High[0], tick[1])
            self.Low[0] = min(Low[0], tick[1])
            self.Close[0] = tick[1]
            self.Dt[0] = tick[0]

    # 计算ma20，只需要参数Open、High、Low、Close、Volume即可，不需要参数tick，因为close就是最新成交价
    def strategy(self):    
        pass
        
        # 计算一个新的MA20
        # 先写一段伪代码
        # ma20 = Close[:19].sum()/20    
        # if new bar is created: # ma20不需要每一个tick（如3秒）都去计算，只需要在创建新bar时计算
        #     sum_ = 0
        #     for item in self.Close[1:21]: #计算Close[1]到Close[20]的平均值，即MA20。注意：list是取头不取尾
        #         sum_ = sum_ + item
        #     ma20 = sum_/20
        
        # # 接下来是比较
        # # 最新值last用Close[0]来代替即可
        # # 条件1：当最新值小于0.95*ma20，就买入
        # if self.Close[0] < 0.95 * ma20:
        #     self.buy()
        # # 条件2：当最新值大于ma20*1.05，就卖出
        # elif self.Close[0] > ma20 * 1.05:
        #     # 子条件2_1：必须先有买入操作，才能才能有卖出操作
        #     if I have long position:    
        #         self.sell()
        #     # 子条件2_2：如果没有买入操作，就跳过，不能执行卖出操作
        #     else:
        #         pass
        # # 条件3：当0.95 * ma20 < 股价 < ma20 * 1.05时，不买不卖，跳过
        # else:
        #     # Close[0] in between 0.95*ma20 and 1.05*ma20, do nothing
        #     pass

    # 因为函数strategy()中用到了函数buy()和sell()，所以先定义这两个函数，否则会报错
    def buy(self):
        pass
    def sell(self):
        pass


#----------------------------------------------------------------------------

# 因为while循环中的函数bar_generator()需要用到参数Dt_, Open_, High_, Low_, Close_, Volume_
# 所以，需要提前赋值给参数Dt_, Open_, High_, Low_, Close_, Volume_
Dt_, Open_, High_, Low_, Close_, Volume_ = \
get_history_data_from_local_machine

trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    # 用变量Dt, Open, High, Low, Close, Volume去接住bar_generator() return的Dt, Open, High, Low, Close, Volume
    # 这里的Dt, Open, High, Low, Close, Volume是6个list，我们可把6个list合并成一个矩阵matrix来做参数传递
    Dt, Open, High, Low, Close, Volume = \
    bar_generator(last_tick, Dt, Open, High, Low, Close, Volume)
    print(last_tick)
    strategy(Dt, Open, High, Low, Close, Volume)
    # trade_time = parser.parse(last_tick[1]).time()
    sleep(3)
print('job done.')

# 视频19:18之后的讲解总结
# # 整个代码的运行逻辑如下：
# 1、从while循环开始运行
# 2、当交易时间符合要求，即While true，那么开始执行代码
# 3、第一步：基于函数getTick()去网页获取最新的股票信息，返回tick，包括成交价、交易日期、交易时间
# 4、第二步：基于函数bar_generator()，通过last_tick去更新Dt, Open, High, Low, Close, Volume
# 5、第三步，基于函数strategy(),通过Dt, Open, High, Low, Close, Volume来执行策略
# 6、第四步：3秒钟之后，重新走while循环，开始第一步

# 从第一步取出参数，放到第二步，第二步返回参数又放到第三步，看上去就非常啰嗦
# 因此，引入“类”(class)的概念，面向对象编程，重构代码，让代码更清晰