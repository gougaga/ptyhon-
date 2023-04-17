import pandas as pd
import numpy as np
# 文件路径
#df = pd.read_csv(r'C:\Users\86186\Desktop\python课程\pandas\my_csv.csv')     # 绝对路径
# 相对路径
df = pd.read_csv('my_csv.csv')
#print(df)
'''基本参数
1.filepath_or_
'''
df1 = pd.read_csv('students2.csv', encoding='gbk')
#print(df1)
# 文件对象
f = open('students2.csv', encoding='gbk')
#print(pd.read_csv(f))

'''sep：读取csv文件是指定的分隔符，默认为逗号。注意：“csv文件的分隔符”和“我们读取csv文件时指定的分隔符”一定要一致'''
dff = pd.read_csv(r'C:\Users\86186\Desktop\python课程\pandas\students_step2.csv', encoding='gbk', sep='|')
#print(dff)



'''delim_whitespace：默认为False，设置为True时，表示分隔符为空白符，可以是空格，“\t”等等。不管分隔符是什么，只要是空白符，那么可以通过delim_whitespace=True进行读取'''
dff1 = pd.read_csv(r'C:\Users\86186\Desktop\python课程\pandas\students_whitespace.txt', delim_whitespace=True)
print(dff1)