#----------------------------------------------------------------------------------------------------chapter 4

#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

import numpy as np
from pandas.core.frame import DataFrame

#使用numpy创建一个同时包含字符串、浮点数和整数的数组，用于存储股票行情数据时，需要按以下方式自定义dtype来实现
deftype = ([('date',  np.str_, 10), ('close', np.float32), ('vol', np.uint32)])
stock = np.array([('2019-01-11', 11.01, 1300000),
                  ('2019-01-12', 12.11, 1200000),
                  ('2019-01-13', 15.01, 1500000),
                  ('2019-01-14', 13.01, 1600000,)], dtype = deftype)
print(stock)
print(type(stock))

#导入Pandas库，并用缩写的别名pd代替pandas
import pandas as pd    
#查看当前安装的pandas库的版本号
print(pd.__version__)   

#4.2 series的生成和访问

#4.2.1 Series的生成方法

#以列表list作为数据类型创建一个series对象
s_list = pd.Series([-1.55666192, 0.127451231, "str-AA", -1.37775038],
                   index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(s_list)

#以ndarray作为数据类型创建一个series对象
s_ndarray = pd.Series(np.arange(4), index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(np.arange(4))
print(s_ndarray)

#以标量值作为数据创建一个series类型
s_scalar = pd.Series(5., index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'], dtype = 'int8')
print(s_scalar)

#以字典作为数据类型创建一个series类型          
s_dict = pd.Series({'2019-01-11':0., '2019-01-12':1., '2019-01-13':2., '2019-01-14':3.})
print(s_dict)

#以字典作为数据类型创建一个series类型，当元素数量少于索引，缺失位置为NaN
s_dict = pd.Series({'2019-01-11':0., '2019-01-12':1.}, index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(s_dict)

#4.2.2 Series的访问方法

#以列表作为数据类型创建一个series对象
series_access = pd.Series([10.23, 11.24, 12.25, 13.26],
                          index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(series_access)

#访问series全部元素数值
print(series_access.values)
#访问series全部索引值
print(series_access.index)
#访问series‘2019-01-11’索引的元素值
print(series_access['2019-01-11'])
#访问series‘2019-01-11’和‘2019-01-13’索引的元素值
print(series_access[['2019-01-11', '2019-01-13']])
#访问series前两个数据的元素值
print(series_access[:2])

#4.3 DataFrame的生成和访问

#4.3.1 DataFrame的生成方法

#以列表组成的字典形式创建DataFrame，创建4行2列的表格
df_list_dict = pd.DataFrame({'Close':[1., 2., 3., 5], 'Open':[1., 2., 3., 4.]},
                            index=['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(df_list_dict)

#以嵌套列表形式创建DataFrame，创建2行4列的表格
df_list_list = pd.DataFrame([[1., 2., 3., 5], [1., 2., 3., 4.]],
                            index = ['2019-01-11', '2019-01-12'],
                            columns = ['Close', 'Open', "low", 'High'])
print(df_list_list)

#以二维ndarray形式创建DataFrame
ndarray_data = np.zeros((2), dtype = [('Close', 'i4'), ('Open', 'f4'), ('Low', 'a10')])
print(np.zeros(2))
print(np.zeros(shape=(2, 4)))
print(ndarray_data)

ndarray_data[:] = [(1, 2., '11.2'),  (2, 3., "12.3")]
df_ndarray = pd.DataFrame(data = ndarray_data, index = ['2019-01-11', '2019-01-12'])
print(df_ndarray)

#以Series组成的字典形式创建DataFrame
series_data = {'Close' : pd.Series([1., 2., 3.], index = ['2019-01-11', '2019-01-12', '2019-01-13']),
               'Open' : pd.Series([1., 2., 3., 4.], index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])}
df_series = pd.DataFrame(series_data)
print(df_series)

#以字典的列表形式创建DataFrame
df_dict_list = pd.DataFrame([{'Close':1, 'Open':2}, {'Close':5, 'Open':10, 'High':20}], index = ['2019-01-11', '2019-01-12'])
print(df_dict_list)

#4.3.2 DataFrame的索引访问

#以Series组成的字典形式创建DataFrame
series_data = {'Close' : pd.Series([10.51, 10.52, 10.53, 10.54], index=['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14']),
                'Open' : pd.Series([12.31, 12.32, 12.33, 12.34], index=['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])}
df_access = pd.DataFrame(series_data)
print(df_access)

#访问DataFrame全部的行索引
print(df_access.index)

#访问DataFrame全部的列索引
print(df_access.columns)

#访问DataFrame全部的行和列索引
print(df_access.axes)

#访问DataFrame全部元素值
print(df_access.values)

#访问DataFrame某列的内容
print(df_access['Open'])
print(df_access.Open)

#查看列类型
print(type(df_access.Open))

#访问某一行内容
print(df_access[0:1])
print(df_access[0:2])
print(df_access[1:2])

#选取了’2019-01-11‘行对应的’Close‘，’Open‘这两列的元素内容
print(df_access.loc[['2019-01-11',], ['Close', 'Open']])

#选取了所有行以及列索引为’Close‘，’Open‘的元素内容
print(df_access.loc[:,['Close', 'Open']])

#访问到'2019-01-11'这行的元素
print(df_access.loc['2019-01-11'])

#选取了前两行，第一列的元素
print(df_access.iloc[0:2, 0:1])

#选取了前两行，所有列的元素
print(df_access.iloc[0:2])

#访问第1行和第3行，第1列和第2列的元素
print(df_access.iloc[[0,2],[0,1]])

#采用混合标签和位置的方式访问元素 从’Open‘列索引中获取第0个和第2个元素
#print(df_access.ix[[0, 2], ['Open']])

#
print(df_access.index[[0, 2]])
print(df_access.loc[df_access.index[[0, 2]], ['Open']])

print(df_access.columns.get_indexer(['Open']))
print(df_access.columns.get_loc('Open'))
print(df_access.iloc[[0, 2], df_access.columns.get_indexer(['Open'])])
print(df_access.index.get_loc('2019-01-12'))

#4.3.5 用条件表达式访问元素

#选取条件是‘Open'列中大于该列平均值，表达式运算后会产生一个True/False值的布尔型Series对象
print(df_access.Open > df_access.Open.mean())

print(df_access[df_access.Open > df_access.Open.mean()])

print(df_access.loc[df_access.Open > df_access.Open.mean(), 'Close'])

#4.4 时间序列的生成和转换

#4.4.1 用datatime生成时间序列

#先导入datetime模块，这里我们指定导入其中的date、time、datetime、timedelta这几个接口
from datetime import date, time, datetime, timedelta

#date.resolution:date对象表示日期的最小单位
print(f'date.resolution: {date.resolution}')
#time.resolution:time对象表示时间的最小单位
print(f'time.resolution: {time.resolution}')
#datetime.resolution:datetime对象表示时间的最小单位
print(f'dateime.resolution: {datetime.resolution}')

#date.max、date.min: date对象所能表示的最大、最小日期范围
print(f'date.max: {date.max} and date.min: {date.min}')
#time.max、time.min: time对象所能表示的最大、最小时间范围
print(f'time.max: {time.max} and time.min: {time.min}')
#datetime.max、datetime.min: datetime对象所能表示的最大、最小时间范围
print(f'datetime.max: {datetime.max} and datetime.min: {datetime.min}')

#构造datetime实例对象
#datetime(year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo]]]]])
datetime_obj = datetime(2016, 10, 26, 10, 23, 15, 1)
print(f'datetime: {datetime_obj}')

#replace用参数指定代替原有对象中的属性生成新的datetime时间对象
re_datetime_obj = datetime_obj.replace(day=27, hour=20)
print(f'datetime: {re_datetime_obj}')
#.isoformat(): 返回型如“YYYY-MM-DD HH:MM:SS"格式的字符串时间
print(f'datetime.isoformat(): {datetime_obj.isoformat()}')
#.strftime(fmt):format自定义格式化时间字
print(f'strftime():{datetime_obj.strftime("%Y-%m-%d %X")}')

#datetime接口也提供了很好用的函数
print(f'datetime.strptime():{datetime.strptime("2016-10-26", "%Y-%m-%d")}')
print(f'fromtimestamp():{datetime.fromtimestamp(1429417200.0)}')
print(f'utcfromtimestamp():{datetime.utcfromtimestamp(1429417200.0)}')
print(f'datetime.now():{datetime.now()}')

#将两个datetime对象直接相减能获得一个timedelta对象，它表示两个日期或时间之间的间隔
delta_obj = datetime.strptime("2019-10-18 04:20:00", "%Y-%m-%d %X") - datetime.strptime("2019-10-01 04:20:00", "%Y-%m-%d %X")
print(type(delta_obj), delta_obj)
print(delta_obj.days, delta_obj.total_seconds())

dt = datetime.now()
#明天后1小时
dt1 = dt + timedelta(days=1, hours=1)
#昨天
dt2 = dt + timedelta(days=-1)
#昨天
dt3 = dt - timedelta(days=1)
print(f"{dt1}\n{dt2}\n{dt3}\n")

#4.4.2用Pandas生成时间序列

#1.基础元素Timestamp

#这里列举了pd.Timestamp()的3种方式
#给定年、月、日、时、分、秒参数值
ts = pd.Timestamp(2019, 1, 1, 2, 3, 4)
print(f'pd.Timestamp()-1: {ts}')
#通过datetime对象转换为时间戳
ts = pd.Timestamp(datetime(2019, 1, 1, hour=2, minute=3, second=4))
print(f'pd.Timestamp()-2: {ts}')
#通过时间格式的字符串转化为时间戳
ts = pd.Timestamp("2019-1-1 2:3:4")
print(f'pd.Timestamp()-3: {ts}')
#转换后的类型为Timestamp
print(f'pd.Timestamp()-type: {type(ts)}')

#这里也列举了pd.to_datetime()的两种方式
#通过datetime对象转换为时间戳
dt = pd.to_datetime(datetime(2019, 1, 1, hour=0, minute=1, second=1))
print(f'pd.to_datetime()-1: {dt}')
#时间格式的字符串转换为时间戳
dt = pd.to_datetime("2019-1-1 0:1:1")
print(f'pd.to_datetime()-2: {dt}')
#转换后的类型为Timestamp
print(f'pd.to_datetime()-type: {type(dt)}')

#通过列表类型的时间字符串直接转换为DatetimeIndex
#pd.to_datetime生成自定义时间序列
dtlist = pd.to_datetime(["2019-1-1 0:1:1", "2019-2-1 0:1:1", "2019-3-1 0:1:1"])
print(f'pd.to_datetime()-list: {dtlist}')

#2.时间偏移Timedelta

#生成一个Timestamp对象dt_0
dt_0 = pd.to_datetime(datetime(2019, 1, 1, hour=0, minute=0, second=0))
#在dt_0上偏移一个Timedelta对象
dt_1 = dt_0 + pd.Timedelta(days=5, minutes=50, seconds=20)
print(f'datetime-1:{dt_0}\ndatetime-2:{dt_1}')

#3.生成时间范围序列

#用pd.date_range()生成时间序列
date_rng = pd.date_range('2019-01-01', freq='M', periods=12)
print(f'month date_range(): \n{date_rng}')

#用pd.period_range()生成时间序列
period_rng = pd.period_range('2019-01-01', freq='M', periods=12)
print(f'month period_range(): \n{period_rng}')
#以上两种生成时间序列方法的区别，详见书P111

#pd.date_range()生成的是周日当天的时间
date_rng = pd.date_range('2019-01-01', freq='W-SAT', periods=12)
print(f'week date_range(): \n{date_rng}')

#pd.period_range()生成的是周一到周日的时间
period_rng = pd.period_range('2019-01-01', freq='W-SUN', periods=12)
print(f'week period_range(): \n{period_rng}')
#说明：经查阅日期得知，2019年1月1日是星期二，之后的第一个周日是1月6日，包含1月1日的那个星期是12月31日到1月6日。

#date_range()会依照起始时间的格式连同分和秒一起显示
date_rng = pd.date_range('2019-01-01 00:00:00', freq='H', periods=12)
print(f'hour date_range(): \n{date_rng}')

#period_range()生成的是时间序列只体现小时格式，这里连同显示了分钟，但并不会显示秒
period_rng = pd.period_range('2019-01-01 00:00:00', freq='H', periods=12)
print(f'hour period_range(): \n{period_rng}')

#4.4.3 时间序列的降采样