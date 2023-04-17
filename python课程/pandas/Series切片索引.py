import pandas as pd
import numpy as np
# 下标索引
s = pd.Series(np.random.rand(5))
print(s)
print('s', s[3], type(s[3]))

# 标签索引
s1 = pd.Series(np.random.rand(5), index=list('abcde'))
print(s1)
print(s1['c'])
print(s1[2])

# 使用索引访问多个元素,需要使用两个中括号 [[]] 相当于中括号[]里面放一个列表
print(s1[['b', 'e']])
# 多标签会创建一个新的
s2 = s1[['b', 'a', 'e']]
print(s2)

'''切片'''
# 通过下标切片的方式访问Series序列中的数据
s3 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('s3::', s3)
# 位置索引就是a，b，c，d，e的下表----0，1，2，3，4
# 标签索引a，b，c，d，e
print(s3['a'])
print(s3[0])
print(s3['a':'c'])  # 包含结束值
# 下标取值可以使用负数取值，不可以使用标签取值’
# 使用位置可以使用切片
print(s3[0:2])    # 不包含结束值



s4 = pd.Series(np.random.rand(15))
print(s4.head())    # 默认显示前五条
print(s4.head(3))   # 显示前三条

print(s4.tail())    # 默认显示后五条
print(s4.tail(2))   # 显示后两条


'''重新索引
使用可选填充逻辑，使Series符合新索引
讲NaN放在上一个索引中没有值的位置。除非新索引等同于当前索引，并生成新对象
'''
s5 = pd.Series(np.random.rand(5), index=list('abcde'))
print(s5)
s6 = s5.reindex(list('cde'))
print(s6)
# fill_value=0 使用0填充
s7 = s5.reindex(list('awz'), fill_value='*')
print(s7)