import numpy as np
import pandas as pd

"""
常用属性和方法汇总
名称  属性&方法描述  
T  行和列转置。  
axes  返回一个仅以行轴标签和列轴标签为成员的列表。  
dtypes  返回每列数据的数据类型。  
empty  DataFrame中没有数据或者任意坐标轴的长度为0，则返回True  
columns  返回DataFrame所有列标签  
shape  返回一个元组，获取行数和列数,表示了 DataFrame 维度。  
size  DataFrame中的元素数量。  
values  使用 numpy 数组表示 DataFrame 中的元素值。  
head()  返回前n 行数据。  
tail()  返回后n 行数据。  
rename()  rename(columns=字典),修改列名  
info()  可以显示信息，例如行数/列数，总内存使用量，每列的数据类型以及不缺少值的元素数  
sort index()  默认根据行标签对所有行排序，或根据列标签对所有列排序，或根据指定某列或某几列对行排序。  
sort values() 既可以根据列数据，也可根据行数据排序
"""
data = {
    'name': ['sjt', 'yjy', 'lyy', 'lxz'],
    'sex': ['m', 'w', 'w', 'w'],
    'age': [20, 20, 20, 20]
}
df = pd.DataFrame(data)
print(df)
# 转置
# 返回DataFrame的转置，也就是把行和列进行交换
print(df.T)
# axes
# 返回一个行标签、列标签组成的列表。
print(df.axes)
# dtypes
# 返回Series，每一列的数据类型。
print(df.dtypes)
# empty
# 返回一个布尔值，判断输出的数据对象是否为空，若True表示对象为空。
print(df.empty)
df1 = pd.DataFrame()
print(df1.empty)
# columns
# 返回DataFrame所有列标签
print(df.columns)
print(len(df.columns))   # 输出有几个列
print(df.columns.size)
# shape
# 返回一个元组，获取行数和列数，表示DataFrame维度。
print(df.shape)         # 第一个是行，第二个是列
# values
# 以ndarray数组的形式返回DataFrame中的数据
print(df.values)
# head()&tail查看数据
print(df.head(3))     # 前3条
print(df.tail(2))     # 后2条
# 修改标签名rename()
# DataFrame.rename(index=None，columns=None，inplace=False)
# #  index: 修改后的行标签
# #  columns: 修改后的列标签
# #  inplace: 默认为False,不改变源数据,返回修改后的数据.True更改源数据
# 可以修改部分行或者列
print(df)
print(df.rename(index={1: 'row2', 2: 'row3'}))
print(df.rename(columns={'name': 'Name', 'age': 'Age'}))
print(df.info())
# 添加参数改变源数据
df1 = df
df1.rename(index={1: 'row2', 2: 'row3'}, columns={'name': 'Name', 'age': 'Age'}, inplace=True)
print(df1.info)
# df1
# info()函数
# 用于打印DataFrame的简要摘要，显示有关DataFrame的信息，包括索引的数据类型dtype和列的数据类型dtype，非空值的数量和内存使用情况
data = {'name': ['郭志阳'], 'age': [20]}   # 需要给列表嵌套
df2 = pd.DataFrame(data)
print(df2)
print(df2.info())
"""
我们来看一看都有些什么信息:
 <class'pandas.core.frame.DataFrame'>:是说数据类型为DataFrame
 Rangelndex: 5 entries，0 to 4:有5条数据(5行)，索引为0-4 
 Data columns (total3 columns): 该数据帧有3列
 #:索引号，不用太在意
 column: 每列数据的列名
 Non-Null count 每列数据的数据个数，缺失值NaN不作计算，可以看出上面Salarv列数据有缺失值
 Dtvpe:数据的类型
 dtypes: float64(1).int64(1).obiect(1)数据类型的统计
 memory usage: 248.0+ bvtes: 该数据帧占用的运行内存(RAM)
"""
df = pd.DataFrame({'b': [1, 2, 2, 3], 'a': [4, 3, 2, 1], 'c': [1, 3, 8, 2]}, index=[2, 0, 1, 3])
print(df)
print(df.sort_index())  # 默认按照行标签升序
# df.sort_index(axis=0, ascending=True)
print(df.sort_index(axis=1))   # 按照列标签升序
df = pd.DataFrame({'b': [1, 3, 2, 3], 'a': [4, 3, 2, 1], 'c': [1, 3, 8, 2]}, index=[2, 0, 1, 3])
print(df)
# 1.按照b列升序排序
df1 = df.sort_values(by='b')
print(df1)
# 2.先按b列降序，再按a列升序排序
df1 = df.sort_values(by=['b', 'a'], ascending=[False, True])
print(df1)
# 3.按行3升序排列
df1 = df.sort_values(by=3, axis=1)
print(df1)
# 4.按行3升序，行0将排列
df1 = df.sort_values(by=[3, 0], axis=1, ascending=[True, False])
print(df1)
"""
注意：指定多列(多行)排序时，先按照排在前面的列(行)排序，如果内部有相同数据，再对相同数据内部用下一个列(行)排序
以此类推。如何内部无重复数据，则后续排列不执行。即首先满足排在前面的参数的排序，再排后面参数
"""
"""
作业
1.用三种不同的方法，创建以下DataFrame(保证columns和index一致，值不做要求)
结果DataFrame为：
    four   one   three   two
a     4     1      3      2
b     5     2      4      3
c     6     3      5      4
d     7     4      6      5
e     8     5      7      6
2.如图创建DataFrame(4*4, 值为0-100的随机数)，通过索引得到以下值
    1）索引得到b，c列的所有值
    2）索引得到第三第四行的数据
    3）按顺序索引得到two，one行的值
    4）索引得到大于50的值
        a           b           c           d
one   60.936882   34.198569   86.933961   63.217850
two   93.910622    8.843498   12.482240   35.940462
three 11.350391   40.704308   50.524502    5.215897
four   5.777448   75.515444   96.847913   57.683561
3.创建一个3*3，值在0-100区间随机值的DataFrame(如图)，分别按照index和第二列值大小，降序排列
创建DataFrame为：
      v1         v2         v3
a   6.477556   9.470260  99.929419
b  47.411645  50.873012  33.376488
c  65.374675  23.431663  43.404255
-------
按照index降序：
      v1         v2         v3
c  65.374675  23.431663  43.404255
b  47.411645  50.873012  33.376488
a   6.477556   9.470260  99.929419
-------
按照第二列值大小降序：
      v1         v2         v3
b  47.411645  50.873012  33.376488
c  65.374675  23.431663  43.404255
a   6.477556   9.470260  99.929419
"""
# 一
# 1.嵌套列表
data = [[4, 1, 3, 2], [5, 2, 4, 3], [6, 3, 5, 4], [7, 4, 6, 5], [8, 5, 7, 6]]
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'], columns=['four', 'one', 'three', 'two'])
print(df)
# 2.字典套列表
data1 = {'four': [4, 5, 6, 7, 8], 'one': [1, 2, 3, 4, 5], 'three': [3, 4, 5, 6, 7], 'two': [2, 3, 4, 5, 6]}
df1 = pd.DataFrame(data1, index=['a', 'b', 'c', 'd', 'e'])
print(df1)
# 3.列表套字典
data = [{'four': 4, 'one': 1, 'three': 3, 'two': 2}, {'four': 5, 'one': 2, 'three': 4, 'two': 3}]
# 指定行标签，列标签
df1 = pd.DataFrame(data, index=['a', 'b'])
print(df1)
# 二
aa = pd.DataFrame(np.array(np.random.rand(16)*100).reshape(4, 4), index=['one', 'two', 'three', 'four'], columns=['a', 'b', 'c', 'd'])
print(aa)
# b, c所有值
print(aa[['b', 'c']])
# 索引得到第三四行的数据
print(aa.iloc[2:])
# 按序
print(aa.loc[['two', 'one']])
# 索引得到大于50值
print(aa[aa > 50])   # aa.values > 50 还是aa > 50 得到的都是布尔值 true false，取值要用布尔索引取值
# 三
aaa = pd.DataFrame(np.array(np.random.rand(9)*100).reshape(3, 3), index=['a', 'b', 'c'], columns=['v1', 'v2', 'v3'])
print(aaa)
print(aaa.sort_index(ascending=False))
print(aaa.sort_values('v2', ascending=False))




