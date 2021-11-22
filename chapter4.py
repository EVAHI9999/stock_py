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


