#! /usr/bin/env python3
#-*- encoding:utf-8 -*-
#

import pandas_datareader.data as web

df_stockload = web.Datareader("000001.SS", "yahoo", datetime.datetime(2009,1,1),datetime.datetime("2019,6,1"))
print(df_stockload.head())