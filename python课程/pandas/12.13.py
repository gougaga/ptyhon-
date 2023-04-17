import numpy as np
import pandas as pd
df = pd.read_csv('./students2.csv',encoding='gbk')
print(df)
df = pd.read_csv('./students2.csv',encoding='gbk',converters={'id':lambda x: int(x) + 10})
print(df)
df = pd.read_csv('./students2.csv',encoding='gbk')
print(df)
df = pd.read_csv('./my.csv',encoding='gbk',true_values=['a'],false_values=['b'])
print(df)
# 这里把第一行过滤掉了，因为第一行是表头，所以在过滤掉之后第二行就变成表头了。
# 当然里面除了传入具体的数值，来表明要过滤掉哪些行，还可以传入一个函数。
df = pd.read_csv('./students2.csv',encoding='gbk',skiprows=[0,3])
print(df)
df = pd.read_csv('./students2.csv',encoding='gbk',skiprows=lambda x: x>0 and x % 2 ==0 )
print(df)
df = pd.read_csv('./students2.csv',encoding='gbk',skipfooter=1,engine='python')
print(df)
df = pd.read_csv('./students2.csv',encoding='gbk',nrows=2)
print(df)
print("---------------------")
df = pd.read_csv('./students2.csv',encoding='gbk')
print(df)
# 要求把朱宇政和地址设置为NaN
# df1 = pd.read_csv('./students2.csv',encoding='gbk',na_values=['朱宇政','克哈星'])
# df1
df = pd.read_csv('./my.csv',encoding='gbk',na_values=['a','apple'])
print(df)
# 把男生设置为Nan
# df2 = pd.read_csv('./students2.csv',encoding='gbk',na_values=['男'])
# df2
df = pd.read_csv('./my.csv',encoding='gbk',na_values=['apple'])
print(df)
# 可以看到将"女"和"朱梦雪"设置成了NaN，这里的情况是不同的列中包含了不同的值
pd.to_datetime()
df = pd.read_csv('./students2.csv',encoding='gbk')
print(df)
print(df.dtypes)
# 转化生日列数据
df1 = pd.read_csv('./students2.csv',encoding='gbk',parse_dates=['birthday'])
print(df)
print(df.dtypes)
df = pd.read_csv('./students_年月日.csv',encoding='gbk')
print(df)