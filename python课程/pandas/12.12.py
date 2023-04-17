# -*-coding:UTF-8 -*-
# def xysz(x):
#     x = str(x)
#     y = 0
#     for i in x:
#         y += int(i)  # 任何9的倍数,各位数的和也是9的倍数
#     a = 9 - y % 9
#     if a == 9:
#         print("对方的幸运数字是0或9")
#     else:
#         print("对方的幸运数字是:", a)
#
#
# xysz()  # 传入对方剩下的数字
import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students_step2.csv',encoding='gbk')
print(df)
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students_step2.csv',encoding='gbk',sep='|')
print(df)
df1 = pd.read_csv(r'./students_whitespace.txt',sep=' ')
print(df1)
df2 =pd.read_csv(r'./students_whitespace.txt',delim_whitespace=True)
print(df2)
# 1.names没有被赋值，header也没被赋值
df = pd.read_csv(r'./students_step2.csv',encoding='gbk')
print(df)
# 2.names没有被赋值，header被赋值
# header=1 选取第2行作为表头（行索引从0开始）第2行下面是数据
df = pd.read_csv(r'./students_step2.csv',encoding='gbk',header=2)
print(df)
# header=None 给自己指定的表头（自定义）
df = pd.read_csv(r'./students_step2.csv',encoding='gbk',names=['编号','姓名','地址','性别','出生日期'])
print(df)
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students2.csv',encoding='gbk')
print(df)
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students2.csv',encoding='gbk',index_col='birthday')
print(df)
print(df.index)
df.index = pd.to_datetime(df.index)
print(df.index)
print(df['2003-10'])
print(df.loc['2002-2-12'])
# 要把birthday当作索引
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students2.csv',encoding='gbk',index_col=['gender','birthday'])
print(df)
print(df.loc['女','2003/8/7'])
df.sort_index(inplace=True)
print(df)
df1 = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students2.csv',encoding='gbk',usecols=['name','gender'])
print(df1)
# 设置数据类型为 str dtype 会以object显示
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students2.csv',encoding='gbk',dtype={'id':str,'name':str})
print(df['id'])
df = pd.read_csv(r'C:\Users\丁琛苧\Desktop\爬虫\students2.csv',encoding='gbk',dtype={'id':float})
print(df['id'])
print(df['name'])















