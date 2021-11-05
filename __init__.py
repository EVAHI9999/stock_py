#! /usr/bin/env python3
#-*- encoding：utf-8 -*-

import keyword
import time


def python_syntax():
    print(keyword.kwlist)

if __name__=='__main__':
    print("This is main function!")
    python_syntax()

print("Quant Trade")

print(10.68)

str_var="Quant trade"
print(str_var)

l_var=[1,2,'a']
print(l_var)

t_var=(1,2,'a')
print(t_var)

d_var={'a':1,'b':2}
print(d_var)

print("This is %s and Price is %2.2f" %("Quant Trade",10.68))

str_time="2019-05-07 21:56:11"
print(f'time is:{str_time}')

print(type(True))
print(type(123))
print(type(1.12))
print(type(3j+1))

a=1
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

print('one quote!')
print('one \' quote!')
print('one “ quote!')
print("two ' quote!")
print("two \" quote!")
print("""three quote!""")
print("""three ' quote!""")
print("""three " quote!""")
print("""three \""" quote!""")

list_temp=['close', 'open', 2019, 2020, [1.1,1.2], "10%"]
print(list_temp[2])
print(list_temp[1:5])
list_temp[2]=2001
print(list_temp)

print(len(list_temp))
print(list_temp.index('open'))
list_temp.append("20%")
print(list_temp)
list_temp.remove(2001)
print(list_temp)

tuple_temp=('close', 'open', 2019, 2020, [1.1, 1.2], "10%")
print(tuple_temp)
print(tuple_temp[1:5])
print(len(tuple_temp))
print(tuple_temp.index(2019))

dict_temp={'chapter1':'content1', 'chapter2':'content1'}
print(dict_temp)
key='chapter3'
dict_temp[key]='content1'
print(dict_temp)

dict_temp={'chapter1':{
                'name':"basic",
                'page':31},
            'chapter2':{
                'name':"senior",
                'page':42
            }
}
print(dict_temp)

print(dict_temp['chapter2'])
print(dict_temp['chapter2']['name'])

dict_temp['chapter3']={'name':"middle",'page':50}
print(dict_temp)

#del dict_temp['chapter2']['name']
#print(dict_temp)
#dict_temp.clear()
#print(dict_temp)
#del dict_temp
#print(dict_temp)

#print(dict_dat.keys())
print(dict_temp.keys())
print(dict_temp.values())
print(dict_temp.items())

def stock_info(name):
    print("this stock is:"+name)

stock_info(u"新希望")

def stock_info_1(name, close, open):
    print(name, close, open)
#stock_info_1(u"新希望", 11.5, 11.8)
#stock_info_1(name=u"新希望", open=11.8, close=11.5)
#stock_info_1(u"新希望", open=11.8, close=11.5)

def stock_info_2(name, open, close=11.5):
    print(name, open, close)

stock_info_2(u"新希望", 11.8, 12)
stock_info_2(u"新希望", 11.8)

def stock_info_3(name, open, close=11.5, *args, **kwargs):

    print("name=", name)
    print("open=", open)
    print("close=", close)
    print("args=", args)
    print("kwargs=", kwargs)

    for i, element in enumerate(args):
        print("args %d-->%s" % (i, str(element)))
    for key in kwargs:
        print("kwargs %s-->%s" % (key, kwargs[key]))

stock_info_3(u"新希望", 11.8, 12, 14, 16, 17)

stock_info_3(u"新希望", 11.8, 12, 14, 16, 17, ave=12, high=15, low=2)

aTuple=(16, 17)
aDict={'ave':12, 'hign':15, 'low':2}

stock_info_3(u"新希望", 11.8, 14, *aTuple, **aDict)

stock_info_3(u"新希望", 11.8, 14, aTuple, aDict)

print(list.__base__)
mylist=[1, 2, 3]
print(mylist.__class__)

#print(mylist.__bases__)
print(list.__class__)

class Human(object):

    century = 21

    def __init__ (self, name, age):
        self.name=name
        self.age=age
        print("init work")

    def speak(self, language):
        print('%s has speak %s ability' % (self.name, language))

    def write(self, word):
        print('%s has write %s ability' % (self.name, word))

    def walk(self):
        print('%s has walk ability' % self)

Allen= Human('Allen-Cart', 16)
# print(Allen.name, Allen.age)
# print(Human.speak, Human.write, Human.walk)
# print(Allen.speak, Allen.write, Human.walk)
# Allen.speak("Chinese")
# Allen.write("Chinese")
# Allen.walk()
# Human.walk('James')
#
# from types import FunctionType, MethodType
# print(isinstance(Human.walk, FunctionType))
# print(isinstance(Allen.walk, MethodType))

print(Human.__dict__)
print(Allen.__dict__)

print(Human.century)
print(Allen.century)

Human.century +=1
print(Human.century)
print(Allen.century)

Allen.century +=1
print(Human.century)
print(Allen.century)

print(Allen.__dict__)

del Allen.century
print(Allen.century)

for i in range(6):
    print(i)

colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, '--->', color)

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
#print(zip(names, colors))
#print(list(zip(names,colors)))
for name, color in zip(names, colors):
    print(name, '--->', color)

import numpy as np

print(np.__version__)

array_1x6 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=np.float64)
print(array_1x6)
print(array_1x6.ndim)
print(array_1x6.shape)
print(array_1x6.dtype)

array_2x6 = np.array([[1.0 ,2.0, 3.0, 4.0, 5.0, 6.0],[1.1, 1.2, 1.3, 1.4, 1.5, 1.6]])
print(array_2x6)
print(array_2x6.ndim)
print(array_2x6.shape)
print(array_2x6.dtype)

array_3x6= np.array([[[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [1.1, 2.1, 3.1, 4.1, 5.1, 6.1], [1.2, 2.2, 3.2, 4.2, 5.2, 6.2]],
                    [[7.0, 8.0, 9.0, 10.0, 11.0, 12.0], [7.1, 8.1, 9.1, 10.1, 11.1, 12.1], [7.2, 8.2, 9.2, 10.2, 11.2, 12.2]]])
print(array_3x6)
print(array_3x6.ndim)
print(array_3x6.shape)
print(array_3x6.dtype)

list_4x3_a=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
list_4x3_b=[[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8]]
list_4x3_c=[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(4):
    for j in range(3):
        list_4x3_c[i][j] = list_4x3_a[i][j] + list_4x3_b[i][j]

print(list_4x3_c)

array_4x3_a = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
array_4x3_b = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]])
print(array_4x3_a + array_4x3_b)

print(array_4x3_a + 5)

array_4x3 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
array_1x3 = np.array([1, 2, 3])
print(array_4x3 + array_1x3)

array_4x3 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(array_4x3)
array_2x1 = np.array([[1], [1]])
print(array_2x1)

# print(array_4x3 + array_2x1)

array_4x3 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
array_4x1 = np.array([[1], [2], [3], [4]])
print(array_4x3 + array_4x1)

array_4x3 = np.array([[1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3], [4.1, 4.2, 4.3]])
print(array_4x3)
print(array_4x3[0])
print(array_4x3[[0], [1]])
print(array_4x3[[True, False, False, False]])
print(array_4x3[[True, False, False, False], 1])
print(array_4x3 <2 )
print(array_4x3[array_4x3 < 2])

from timeit import timeit
from timeit import repeat

def timeit_test(number=3, repeat=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeat):
                start = time.perf_counter()
                for _ in range(number):
                    func(*args, **kwargs)
                elapsed = (time.perf_counter() - start)
                print('Time of {} used: {}'.format(i, elapsed))
        return wrapper
    return decorator


@timeit_test(number=1, repeat=1)
def list_test():
    my_list = list(range(1000000))

@timeit_test(number=1, repeat=1)
def ndarray_test():
    my_arr = np.arange(1000000)

list_test()
ndarray_test()

@timeit_test(number=1, repeat=1)
def list_test():
    my_list = []
    for num in range(1000000):
        my_list.append(num * 2.0)

@timeit_test(number=1, repeat=1)
def ndarray_test():
    my_arr = np.arange(1000000)
    my_arr = my_arr * 2.0

list_test()
ndarray_test()

array_one = np.ones(shape=(2, 4))
print((array_one))

array_full = np.full(shape=(2, 4), fill_value=10)
print(array_full)

array_eye = arr_eys =np.eye(4, M=10)
print(array_eye)

array_linspace = np.linspace(start=0, stop=5, num=10, endpoint=False)
print(array_linspace)

array_randint = np.random.randint(1, 4, size=10)
print(array_randint)

array_binomial = np.random.binomial(1, 0.5, size=10)
print(array_binomial)

array_randn = np.random.randn(3, 4)
print(array_randn)

array_rand = np.random.rand(3, 4)
print(array_rand)

array_normal = np.random.normal(loc=10.0, scale=1.0, size=(1, 3, 2))
print(array_rand)

array_4x3_234 = np.array([[1, 0, 1], [-2, 2, 2], [3, -3, 3], [4, 4, -4]])
array_sign = np.sign(array_4x3_234)
print(array_sign)

array_4x3_235 = np.array([[1, 1, 1], [-2, np.nan, 2], [3, np.nan, 3], [4, 4, -4]])
array_isnan = np.isnan(array_4x3_235)
print(array_isnan)

array_4x3_236 = np.array([[1, 1, 1], [-2, 8, 2], [3, 9, 3], [4, 4, -4]])
array_where = np.where(array_4x3_236 > 5, 5, 0)
print(array_where)

matrix_a = np.mat('1 3 5; 2 4 6')
matrix_b = np.mat([[1, 3, 5], [2, 4, 6]])
print(matrix_a)
print(matrix_b)

print(type(matrix_a))
print(type(matrix_b))

array_c = np.array([[1, 3, 5], [2, 4, 6]])
print(array_c)

print(type(array_c))

array_1 = np.random.rand(4, 4)
print(array_1)
print(type(array_1))
matrix_1 = np.mat(array_1)
print(matrix_1)
print(type(matrix_1))

A = np.mat([[1, 2], [3, 4]])
B = np.mat([[1, 2], [3, 4]])
print(np.dot(A, B))

A = np.mat([[1, 2], [3, 4]])
B = np.linalg.inv(A)
print(A)
print(B)

A = np.mat([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
B = np.mat([[6], [-4], [27]])
print('计算：A^(-1)B:')
X = np.linalg.solve(A,B)
print(X)

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