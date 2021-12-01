#! /usr/bin/env python3
#-*- encoding：utf-8 -*-
# http://hq.sinajs.cn/?format=text&list=sh600519

# ----------P14 11.3_类的实例化，调取类的属性----------
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
        
        # 类不需要return
        # 但，可以写一个return，以检验类中的方法是否被成功执行，如下：
        return 1
        
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
# 类的实例化，其名称为ast
# 当类实例化之后，就会去跑AstockTrading中的method，去内存开辟空间
ast = AstockTrading()
# print(ast)的结果为：<__main__.AstockTrading object at 0x0000000009DEC9D0>
# 其中：0x0000000009DEC9D0，是内存地址
print(ast)
# 调用ast里面的Dt，因ast里面的Dt为None，因此输出None
print(ast.Dt)
print(ast.Open)
print(ast.High)
# 以上print结果都是None
# 我们接着跑get_history_data_from_local_machine()
# 因为在get_history_data_from_local_machine()中添加了return 1，因此打印结果是1
# 这里的重点不是返回1，而是修改了Open和High
print(ast.get_history_data_from_local_machine())
# 重新调用ast的High,其打印结果就是[2, 3, 4]
print(ast.High)
# 重新调用ast的Open,其打印结果就是[1, 2, 3]
print(ast.Open)

# 以上，我们就有历史数据了
# 接下来，去网页获取最新的tick
trade_time = time(9, 30)
while time(9) < trade_time < time(15):
    last_tick = getTick()
    # 更新bar
    ast.bar_generator(last_tick)
    # 调用策略，确定买卖
    ast.strategy()
    trade_time = last_tick[1]
    sleep(3)  
print('job done.')

# 视频13:58之后的讲解总结
# # 整个代码的运行逻辑如下：
# 1、第一步：实例化类
# 2、第二步：调类里面的get_history_data_from_local_machine()修改K线的开高低收，从None变成实际值
# 3、第三步：进入while循环
#           获取最新报价
#           更新K线
#           调用策略
#           休息3秒，重新开始while循环