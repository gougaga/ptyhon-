import numpy as np
#创建4行2列的随机数据
a = np.random.rand(4,2)
print(a)
# 穿件两款2行3列的随机数据
b = np.random.rand(2,2,3)
print(b)
"""
from matplotlib import pyplot as plt
a= np.random.randn(10)
print(a)
# 直方图
plt.hist(a)
"""
# 正态分布
c = np.random.normal(loc=0.0,scale=1.0,size=None)
a = np.random.normal(loc=0.0,scale=1.0,size=None)
print(a)


a = np.random.randint(10,size=5)
print(a)
b = np.random.randint(2,10,size=5)
print(b)
np.random.randint(2,10,size=(2,5))
#随机1-5
num = np.random.randint(1,5)
print(num)

#随机种子 使用相同的seed()职责每次生成的随机数相同使用随机数可以预测
# 但是只有在调用的时候seed()一下并不能使用随机数相同需要每次调用
np.random.seed(2)
L1 = np.random.randn(3,3)
np.random.seed(2)
L2 = np.random.randn(3,3)
print(L1)
print('!!!!!!!!!!')
print(L2)

# 返回半开区间内的浮点数【0.0，1.0】
a = np.random.sample((2,3))
print(a)
b = np.random.sample((2,2,3))
print(b)

#标准的正态分布
np.random.normal(0,1,(3,2))
print(a)
# 均值1 标准差3
np.random.normal(1,3,(3,2))
print(b)


a = np.array([[1,2,3],[4,5,6]])
print(a)
# 数组形状
#print(a,shape)
# 三行三列（numpy.resize()）
b = np.resize(a,(3,3))
print(b)
# 三行三咧（ndarray.resize()）
a.resize((3,3),refcheck=False)
print(a)

a = np.array([[1,2,3],[4,5,6]])
print(a)
# 向a添加元素
print(np.append(a,[7,8,9]))
# 指定轴axis=0
print(np.append(a,[[7,8,9]],axis=0))
# 指定axis=1
print(np.append(a,[[5,5,5],[7,8,9]],axis=1))


a = np.array([[1,2],[3,4],[5,6]])
print(a)
# 不指定 axis情况 返回数组一维
print(np.insert(a,3,[11,12]))
# 不指定 axis=0
print(np.insert(a,1,[11],axis=0))
# 不指定 axis = 1（按照列插入不用中括号）
print(np.insert(a,1,11,axis=1))