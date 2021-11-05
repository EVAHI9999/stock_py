#----------------------------------------------------------------------------------------------------chapter 4

#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

import numpy as np

deftype = ([('date',  np.str_, 10), ('close', np.float32), ('vol', np.uint32)])
stock = np.array([('2019-01-11', 11.01, 1300000),
                  ('2019-01-12', 12.11, 1200000),
                  ('2019-01-13', 15.01, 1500000),
                  ('2019-01-14', 13.01, 1600000,)], dtype = deftype)
print(stock)
print(type(stock))

import pandas as pd
print(pd.__version__)

s_list = pd.Series([-1.55666192, 0.127451231, "str-AA", -1.37775038],
                   index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(s_list)

s_ndarray = pd.Series(np.arange(4), index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(s_ndarray)

s_scalar = pd.Series(5., index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'], dtype = 'int8')
print(s_scalar)

s_dict = pd.Series({'2019-01-11':0., '2019-01-12':1., '2019-01-13':2., '2019-01-14':3.})
print(s_dict)

s_dict = pd.Series({'2019-01-11':0., '2019-01-12':1.}, index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(s_dict)

series_access = pd.Series([10.23, 11.24, 12.25, 13.26],
                          index = ['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(series_access)

print(series_access.values)
print(series_access.index)
print(series_access['2019-01-11'])
print(series_access[['2019-01-11', '2019-01-13']])
print(series_access[:2])

df_list_dict = pd.DataFrame({'Close':[1., 2., 3., 5], 'Open':[1., 2., 3., 4.]},
                            index=['2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14'])
print(df_list_dict)

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