import pandas as pd
import numpy as np
# 选取数据列表
# 可以使用列索引，轻松实现数据选取
data = {'name': ['zzz', 'sss', 'aaa'], 'sex': ['男', '男', '女'], 'age': [220, 20, 22]}
# 定义标签
index = ['stu1', 'stu2', 'stu3']
# 使用字典创建
df = pd.DataFrame(data, index=index)
print(df)
# 只取出name列的数据
print('只取出name列的数据', df['name'])
# 只取出sex列的数据
print('只取出sex列的数据', df['sex'])
# 同时获取name列和sex列数据
print('同时获取name列和sex列数据', df[['name', 'sex']])
# 不能使用切片取值;不可以使用标签下标取值
'''
列的添加
   使用colimns列索引标签可以实现添加先的数据列
'''
df['score'] = [80, 80, 80]
print(df)
# 将已经有的列进行计算得到新的列
df['rating'] = df['age'] + df['score']
print(df)
'''
insert()插入方法
   loc：整形，插入索引，必须0<=loc<=len(列)
   column：插入列的标签，类型可以是（字符串/数字/散列对象）
   value：数值，Series或者数组
   alow_duplicates:允许重复，可以有相同的列标签，默认为Fales
'''
df.insert(5, column='niybi', value=[999, 888, 666])
print(df)
df.insert(6, column='niybi', value=[99, 88, 66], allow_duplicates=True)
print(df['niybi'])
'''
删除列
  通过del和pop（）都能够删除DataFrame中的数据列，opo有返回值
'''
# del删除
del df['age']       # 没有返回值
print(df)
# pop删除
a = df.pop('sex')    # 有返回值，返回值是删除的东西
print(a)
print('**************************')
print(df)