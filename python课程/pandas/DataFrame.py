import pandas as pd
import numpy as np

# DdataFrame 是一个二维数组结构，类似与二维数组


# 使用普通列表创建
print('-------普通列表创建----------')
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
data = [1, 2, 3, 4, 5]
se = pd.Series(data)
print(se)
print('----------------------------------------------------')

# 使用嵌套列表创建
print('-----------嵌套列表创建-------------')
data = [['zql', 20], ['cb', 20], ['lqw', 19]]
df = pd.DataFrame(data)
print(df)
print('----------------------------------------------')
# 指定列标签
data = [['zql', 20], ['cb', 20], ['lqw', 19]]
df = pd.DataFrame(data, columns=['name', 'age'])
print(df)
print('-------------------------------------------')

# 指定数值元素的数据类型位 float
# dtype只能设置一个，设置多个列的数据类型，需要使用其他方式
print('----------指定数值元素的数据类型位-------')
data = [['cm', 19, '女', 20000], ['lsg', 20, '男', 200], ['hhh', 222, '男', 2]]
# 分配列标签
df = pd.DataFrame(data, columns=['name', 'age', 'sex', 'money'], dtype=int)
# int 满足某列特征会自动使用，不满足会自动识别
print(df)
print(df['money'].dtype)
print(df['name'].dtype)
print('--------------------------------------------')

# 字典嵌套列表创建
# data字典中，键对应的值的元素长度必须相同(也就是列表长度相同)。如果传递了索引，那么索引的长度应该等于数组的长度；如果没有传递索引，那么默认情况下，索引将是Rangelndex(0.1...n)，其中n代表数组长度。
print('---------字典嵌套列表创建-------')
data = {'name': ['蔡萌是傻逼', '蔡萌小傻逼', '蔡萌大傻逼'], 'age': [18, 19, 20]}
# 通过字典创建
df = pd.DataFrame(data)
print(df)
# 输出标签
print(df.index)
print(list(df.index))
print('---------------------------------------------------')

# 添加自定义的行标签
print('--------添加自定义的行标签-----')
data = {'name': ['蔡萌是傻逼', '蔡萌小傻逼', '蔡萌大傻逼'], 'age': [18, 19, 20]}
# 通过字典创建
# 添加行标签
index = ['stu1', 'stu2', 'stu3']
df = pd.DataFrame(data, index=index)
print(df)
# 输出标签
print(df.index)
print(list(df.index))
print('---------------------------------------------------')

# 列表嵌套字典创建DataFrame对象
# 列表嵌套字典可以作为输入数据传递给DataFrame构造函数。默认情况下，字典的键被用作列名
print('-------列表嵌套字典创建DataFrame对象-------')
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 100}]
df = pd.DataFrame(data)
print(df)
print('------------------------------------------------')

# 如何使用列表嵌套字典创建一个DataFrame对象， 可以设置结果需要哪些列
print('---使用列表嵌套字典创建一个DataFrame对象---')
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 100}]
# 指定行标签， 列表前
df = pd.DataFrame(data, index=['num1', 'num2'], columns=['a', 'b'])
print(df)
print('***********************')
# 注意：因为d在字典中不存在，所以对应值位NaN
df2 = pd.DataFrame(data, index=['num1', 'num2'], columns=['a', 'd'])
print(df2)

# Series创建DataFrame对象
# 也可以传递一个字典形式的Series，从而创建一个DataFrame对象，其输出结果的行索引是所有index的合集
print('-----Series创建DataFrame对象-----')
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df11 = pd.DataFrame(d)
print(df11)