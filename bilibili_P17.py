#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

# ----------P16 13.2_完善MA策略----------
# 本节课重点是把策略写好，因为strategy()里面有一些伪代码在里面。

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
        # 因method strategy()里面需要用到“新bar是否被创建”的逻辑判断
        # 所以我们新建属性_isNerBar，并赋值为False
        self._isNerBar = False
        
        
        # 因method strategy()里面需要判断我们是否已经有仓位
        # 所以我们新建属性_current_orders，并用
        # dict,字典
        # 来存储信息
        # 这里先随便赋值如下
        # open_price：买入价；
        # open_datetime：买入时间；
        # comment：其他信息
        # 有关current_orders是如何判断是否有仓位的用法，见本文件最下方
        self._current_orders = {
            'order1': {
                'open_price': 1,
                'open_datetime': '2021-10-22 9:00',
                'comment': {}
                }
            }
        
        # 因为我们需要有个容器储存历史交易
        # 因此新建属性self._history_orders
        self._history_orders = {
            }

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
            
            # 因为strategy(self)里面需要判断ner bar是否被创建
            # 所以，在执行完以上代码时，需要修改属性self._isNerBar的值为True
            # 与此同时，在else里面需要将self._isNerBar的值改为False
            self._isNerBar = True
             
        else:
            self._High[0] = max(self._High[0], self._tick[1])
            self._Low[0] = min(self._Low[0], self._tick[1])
            self._Close[0] = self._tick[1]
            self._Dt[0] = self._tick[0]
            # 承接上面的if
            # 在程序执行完else的代码之后，需要将self._isNerBar的值改为False
            self._isNerBar = False
    
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
 
        
        # 如何判断new bar是否被创建？
        # 第一步，在__init__(self)里面新建属性self._isNerBar
        # 第二步，在bar_generator(self)里面修改属性self._isNerBar
        #       2.1 在bar_generator(self)的if里面添加self._isNerBar = True
        #       2.1 在bar_generator(self)的else里面添加self._isNerBar = False
        # 因此，下面这样代码
        # if new bar is created:
        # 可以改为
        if self._isNerBar: # 这里无需写成 self.__isNerBar ==  True
            sum_ = 0
            for item in self.Close[1:21]: 
                sum_ = sum_ + item
            ma20 = sum_/20
        
        # 先判断我们是空仓
        # 如何判断我们是否已经有仓位？
        # 第一步，在__init__(self)里面新建属性self._current_orders
        # 第二步：理解如何用self._current_orders的长度判断是否空仓，见本文件最下方
        # 第三步：将如下代码
        # if we have not long position:
        # 改为
        if 0 == len(self._current_orders) #len == 0 表示空仓
            if self.Close[0] < 0.95 * ma20:
                self._buy()
        else:
            if self.Close[0] > ma20 * 1.05:  
                self._sell()  

#----------------------------------------------------------------------------
ast1 = AstockTrading('600036')
ast1.get_history_data_from_local_machine()

trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    ast1.bar_generator(last_tick)
    ast1.strategy()
    trade_time = last_tick[1]
    sleep(3)  
print('job done.')

ast2 = AstockTrading('601318')
print(ast1)
print(ast2)


# 通过判断字典的长度来判断我们是否有仓位

# 当我们有一笔买入时，字典如下：
current_orders = {
    'order1': {'open_price': 1,'open_datetime': '2021-10-22 9:00'}
}
# 字典长度为：1
print(len(current_orders))

# 当我们有两笔买入时，字典如下：
current_orders = {
    'order1': {'open_price': 1,'open_datetime': '2021-10-22 9:00'},
    'order2': {'open_price': 2,'open_datetime': '2021-10-23 9:00'}
}
# 字典长度为：2

print(len(current_orders))
# 当我们空仓或清仓时，字典如下：
current_orders = {}
# 字典长度为：0
print(len(current_orders))