import pandas as pd
import numpy as np

ar_list = [3, 10, 4, 5]
print(type(ar_list))
# 使用列表创建
s1 = pd.Series(ar_list)
print(s1)
print((type(s1)))

# 使用数组创建
np_arr = np.arange(1, 6)
print(type(np_arr))
s2 = pd.Series(np_arr)
print(s2)
print(type(s2))

# 通过index和values属性取得对应的标签和值
a = list(s2.index)
print('ss', a)
# 通过values取值
print(s2.values, type(s2.values))
# 通过标签取值
print(s2[1])

# 修改值
s2[5] = 50
print(s2)
# 添加标签为-1的元素
s2[-1] = 100
print(s2)
print(s2[-1])   # 存在-1标签

# 字典作为数据源创建Series
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(d)
print(ser)
# 通过index和values属性取得对应的标签和值
print(ser.index)
print(ser.values)
# 取值
print(ser['a'])
# 修改值


# 如果标签是非数值类型，可以使用下标取值（0，1，2，3，4............）
print(ser[2])
# 使用下标 -1 可以取值
print(ser[-1])

d2 = {'a': 5, 'b': 2, 'c': 3}
s3 = pd.Series(d2)
print('11111', s2.index)

# 通过标量创建
