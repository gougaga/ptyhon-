import pandas as pd
import numpy as np
data = {
    'Name': ['关羽', '刘备', '张飞', '曹操'],
    'Age': [28, 64, 29, 42],
    'Salary': [5000, 8000, 4500, 10000],
    'hobby': ['python', 'java', 'go', 'JavaScript']
}
# 定义行标签
index = ['rank1', 'rank2', 'rank3', 'rank4']
# 通过字典创建DataFrame
df = pd.DataFrame(data, index=index)
print(df)
# 取得第三行数据
print('----------------------')
print(df.loc['rank3'])
# 取得Age列的数据
print('/////////////////////')
print(df['Age'])
# 取得Age和Salary列数据
print('*************************')
print(df[['Age', 'Salary']])
# 取得前三行数据
print('+++++++++++++++++++++++++++++')
print(df.iloc[0:3])
# 取得前三行Name|Age|Salary数据
print('================================')
print(df.iloc[0:3][['Name', 'Age', 'Salary']])
# 取得行1和3.列Age和Salary数据
print('8888888888888888888888888888888888888888888')
print(df.iloc[[0, 2]][['Age', 'Salary']])