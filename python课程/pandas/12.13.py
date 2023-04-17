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
# ����ѵ�һ�й��˵��ˣ���Ϊ��һ���Ǳ�ͷ�������ڹ��˵�֮��ڶ��оͱ�ɱ�ͷ�ˡ�
# ��Ȼ������˴���������ֵ��������Ҫ���˵���Щ�У������Դ���һ��������
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
# Ҫ����������͵�ַ����ΪNaN
# df1 = pd.read_csv('./students2.csv',encoding='gbk',na_values=['������','�˹���'])
# df1
df = pd.read_csv('./my.csv',encoding='gbk',na_values=['a','apple'])
print(df)
# ����������ΪNan
# df2 = pd.read_csv('./students2.csv',encoding='gbk',na_values=['��'])
# df2
df = pd.read_csv('./my.csv',encoding='gbk',na_values=['apple'])
print(df)
# ���Կ�����"Ů"��"����ѩ"���ó���NaN�����������ǲ�ͬ�����а����˲�ͬ��ֵ
pd.to_datetime()
df = pd.read_csv('./students2.csv',encoding='gbk')
print(df)
print(df.dtypes)
# ת������������
df1 = pd.read_csv('./students2.csv',encoding='gbk',parse_dates=['birthday'])
print(df)
print(df.dtypes)
df = pd.read_csv('./students_������.csv',encoding='gbk')
print(df)