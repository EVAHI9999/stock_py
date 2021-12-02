#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

# ----------P16 13.1_用类改造此前面向过程写的代码----------
# 本节课重点是改造代码

import requests
from time import sleep
from datetime import datetime, time
from dateutil import parser

# 先定义一个类
class AstockTrading(object):
    # 定义类的第一步就是写一个构造函数，__init__()
    def __init__(self):
        # 定义类的第二步就是把我们所需要的属性都放在构造函数里
        # 属性 -> attributes
        # 我们先添加高开低收和时间属性，其他属性，我们有需要时，再添加
        self._Open = []  #用列表来存放这些数据
        self._High = []
        self._Low = []
        self._Close = []
        self._Dt = []
        # 因methond bar_generator()里面用到了属性_Volume
        # 所以我们新增属性_Volume
        self._Volume = []
        # 因methond getTick()里面用到了属性_tick
        # 所以我们新增属性_tick，并赋值为None
        self._tick = None
        # 因methond bar_generator()里面用到了属性_last_bar_start_minute
        # 所以我们新增属性_last_bar_start_minute，并赋值为None
        self._last_bar_start_minute = None
        

    # 缩进之前写的函数getTick()，并在函数括号内加上self
    # getTick()就不是function了，而是一个method
    def getTick(self):
        page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600519")
        stock_info = page.text
        mt_info = stock_info.split(",")
        last = float(mt_info[3])
        trade_datetime = mt_info[30] + ' ' + mt_info[31]
        # 参数tick，改成self._tick
        # 因此，我们需要在__init__属性里加一个self._tick
        # 本视频8：30，作者将(last, trade_datetime) 顺序改成了( trade_datetime, last)   
        self._tick = (last, trade_datetime)   
        
        # 从function改成method之后，就不需要return了
        # return tick
        
    # 接下来改get_history_data_from_local_machine
    # 1、缩进
    # 2、加self
    def get_history_data_from_local_machine(self):
        # self.Open = [1, 2, 3]
        # self.High = [2, 3, 4]
        
        # 因为，我们还没到实盘交易
        # 所以，这部分代码先pass
        pass

    # 接下来改bar_generator
    # 1、缩进
    # 2、去掉function bar_generator()的参数tick、Dt、Open、High、Low、Close、Volume
    # 3、新增mehond bar_generator()的参数self
    def bar_generator(self):
        
        # last_bar_start_minute需要变成属性
        # 否则，每次调用bar_generator()时，bar_generator()是都会被赋值为None
        # last_bar_start_minute = None
        
        # 将tick改成self._tick.
        # 将last_bar_start_minute改成self._last_bar_start_minute
        # 将Open改成self._Open
        # 将High改成self._High
        # 将Low改成self._Low
        # 将Close改成self._Close
        # 将Dt改成self._Dt
        if self._tick[0].minute % 5 == 0 and \
            self._tick[0].minute != self._last_bar_start_minute:
            self._last_bar_start_minute = self._tick[0].minute
            self._Open.insert(0, self._tick[1])
            self._High.insert(0, self._tick[1])
            self._Low.insert(0, self._tick[1])
            self._Close.insert(0, self._tick[1])
            self._Dt.insert(0, self._tick[0])
             
        else:
            self._High[0] = max(self._High[0], self._tick[1])
            self._Low[0] = min(self._Low[0], self._tick[1])
            self._Close[0] = self._tick[1]
            self._Dt[0] = self._tick[0]
    
    # 接下来改buy()和sell()
    # 1、缩进
    # 2、加self
    # 3、在buy()和sell()前面加下划线“_”，表示内部使用的method
    def _buy(self):
        pass
    def _sell(self):
        pass

    # 接下来改strategy()
    # 1、缩进
    # 2、去掉function strategy()的参数Dt、Open、High、Low、Close、Volume
    # 3、新增mehond strategy()的参数self
    # 4、将Close改成self._Close
    # 5、将buy()和sell()改成self._buy()和self._sell()
    def strategy(self):    
 
        if new bar is created: 
            sum_ = 0
            for item in self.Close[1:21]: 
                sum_ = sum_ + item
            ma20 = sum_/20
        
        if self.Close[0] < 0.95 * ma20:
            self._buy()
        elif self.Close[0] > ma20 * 1.05:
            if I have long position:    
                self._sell()
            else:
                pass
        else:
            pass    
    
# __init__，构造， 初始化， 实例化
# self 可以自由改成this， that， AtraderX
class AstockTrading(object):
    # 每一个函数都可以传递参数，如下面的__init__()
    # 如果函数有参数，在实例化类的时候，就需要有参数，如下修改：
    # ast1 = AstockTrading('600036') # 给招行
    # ast2 = AstockTrading('601318') # 给平安
    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.Dt = None
        self.Open = None
        self.High = None
        self.Low = None
        self.Close = None
        self.Volume = None
        
    #更新历史数据

        


    # 计算ma20，只需要参数Open、High、Low、Close、Volume即可，不需要参数tick，因为close就是最新成交价




#----------------------------------------------------------------------------
# 类的实例化，其名称为ast1，给招行
ast1 = AstockTrading('600036')
ast1.get_history_data_from_local_machine()

trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    # 更新bar
    ast1.bar_generator(last_tick)
    # 调用策略，确定买卖
    ast1.strategy()
    trade_time = last_tick[1]
    sleep(3)  
print('job done.')

# 类的实例化，其名称为ast2，给平安
ast2 = AstockTrading('601318')

# print(ast1)的输出结果是：
# <__main__.AstockTrading object at 0x0000000009E1CFD0>
print(ast1)
# print(ast2)的输出结果是：
# <__main__.AstockTrading object at 0x0000000009E1CDC0>
print(ast2)
# 对比以上两个输出结果，可以发现
# ast1和ast2的内存地址是不一样的

# self的作用
# 当第一次实例化时，即，ast1 = AstockTrading()时，self就指向ast1
# 当第一次实例化时，即，ast2 = AstockTrading()时，self就指向ast2
# 所以，self就实现了“封闭”，实现了一个闭环

# __init__的作用
# __init__就是构造函数
构造函数的目的就是，创建所需的属性