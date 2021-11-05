#----------------------------------------------------------------------------------------------------chapter 4

#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

import numpy as np

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

ndarray_data = np.zeros((2), dtype = [('Close', 'i4'), ('Open', 'f4'), ('Low', 'a10')])
print(ndarray_data)

ndarray_data[:] = [(1, 2., '11.2'),  (2, 3., "12.3")]
df_ndarray = pd.DataFrame(data = ndarray_data, index = ['2019-01-11', '2019-01-12'])
print(df_ndarray)

series_data = {'Close' : pd.Series([1., 2., 3.], index = ['2019-01-11', '2019-01-12', '2019-01-13']),
               'Open' : pd.Series([1., 2., 3., 4.], index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])}
df_series = pd.DataFrame(series_data)
print(df_series)

df_dict_list = pd.DataFrame([{'Close':1, 'Open':2}, {'Close':5, 'Open':10, 'High':20}], index = ['2019-01-11', '2019-01-12'])
print(df_dict_list)