import pandas as pd
import numpy as np
'''
4.添加数据行
使用append()函数，可以将新的数据行添加到DataFrame中，该函数会在行未追加数据行df.append(other,ignore_index=False
verify_integrity=False,sort=False)
将"other"追加到调用者的末尾，返回一个新对象。"other"行中不在调用者中的列将作为新列添加。
·other:DataFrame或Series/dic类对象，或这些对象的列表
•ignore_index：默认为False，如果为True将不适用index标签.
•verify_integrity：默认为False如果True，则在创建具有重复项的索引时引发ValueError.
•sort:排序

'''


data = {'name': ['zzz', 'sss', 'aaa'], 'sex': ['男', '男', '女'], 'age': [220, 20, 22]}
# 定义标签
index = ['stu1', 'stu2', 'stu3']
df = pd.DataFrame(data, index=index)
print(df)

'''追加字典'''
# 如果不给ignore_index=True会报错
d2 = {'name': 'lxx', 'sex': '女', 'age': 20}
fd1 = df.append(d2, ignore_index=True)
print(fd1)

'''追加Series数据,有name参数'''
# 1.给参数：ignore_index=True； 2.给序列名
print('------------------------------------------------')
d3 = {'name': 'ksx', 'sex': '女', 'age': 20}
s = pd.Series(d3, name='a')
df2 = df.append(s)
print(df2)

'''追加列表
-- 如果list是一维的，则以列的形式追加
-- 如果list是二维的，则以行的形式追加
-- 如果list是三位的，只添加一个值
    注意：使用append可能会出现相同的index，想避免的话可以使用ignore_index=True
'''
print('************************************************')
data1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
df1 = pd.DataFrame(data1)
print(df1)
print('//////////////////////////////////////')
a1 = [20, 30]
df3 = df1.append(a1, ignore_index=True)
print(df3)

#list是一维，则以列的形式追加

a2 = [[10, '20', 30]]
df4 = df1.append(a2, ignore_index=True)
print('||||||||||||||||||||||||||||||||||||||||||||||')
print(df4)

'''删除数据行
 标签存在重复会被一起删除
 ...drop方法不会改变数据源
'''
print('111111111111111111111111111111111111111111111111111')
de = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
de2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
de = de.append(a2)
print(de)
de1 = de.drop(0)
print('``````````````````````````````````````````')
print(de1)








