import pandas as pd
import numpy as np
# 使用"显示索引"的方法定义索引标签
data = np.array(['a', 'b', 'c', 'd'])
b = pd.Series(data, index=[100, 101, 102, 103])
print(b)

# 从指定索引的字典构造序列
d = {'a': 1, 'b': 2, 'c': 3}
a1 = pd.Series(d, index=['a', 'b', 'c'])
print(a1)

# 当传递的索引值未匹配对应的字典键时，使用NAN（非数字）填充
a2 = pd.Series(d, index=['a', 'p', 'w'])
print(a2)

# 请注意，索引时首先使用字典中的键构建的。在此之后，用给定的索引值对序列重新编制索引，因此我们所得到所有NaN

# 通过匹配的索引值，改变创建Series数据的顺序
a3 = pd.Series(d, index=['c', 'a', 'b'])
print(a3)

'''           name参数
我们可以给Series对象命名， 也可以给一个Series数组中的索引列起一个名字，pandas为我们设计好了对象属性，并在设置了name属性值用来进行名字的设定
'''
data1 = {
    'bj': 2000,
    'sh': 2500,
    'sz': 1800
}
qq = pd.Series(data1)
print('ss', qq)
qq.name = 'city data'
qq.index.name = 'city name'
print(qq)

# copy表示对data进行拷贝， 默认为False，仅影响Series和ndarray数组
n1 = np.arange(1, 6)
print(n1)
sn1 = pd.Series(n1)
print(sn1)
sn1[4] = 99
print(sn1)
n2 = [1, 2, 3, 4, 5]
print(n2)
sn2 = pd.Series(n2)
print(sn2)
sn2[4] = 100
print(sn2)
