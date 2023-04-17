import numpy as np
"""
统计函数 从数组中快速查询最小，最大，百分位标准差
amin（）参数：axis  1行必、0例比
amax（）
ptp（） 最大值-最小值的差
percentile（）度量，百分比  1.数组 2.半分比 0-100 3.axis
median（） 计算数组的 （中位数） 中值
mean（） 算数平均值
std（） 标准差 sqrt（mean（x-x，mean（））**2）
        标准差是一组数组的平均值分散策成的一种度量
        标准差应用于投资上，可作为度量回报稳定性的指标。标准数值差越大，代表汇报远离过去平均数值，回报较不稳定姑风险越高。相反，标准差数
var（）方差mean（（x-x.mean（）**2）
        平均数之差的平方的平均数
        衡量随机变量或一组数据时离散程度的度量
求和 ndarray.sun（）
axis = 0，从上往下查找：'，ml.sum（axis=0）
axis = 1，从左往右查找：'，ml.sum（axis=1）


加权平均值 numpy.average()
即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数
numpy. average(a, axis=None, weights=None, returned=False)
-weights:数组，可选

与a中的值关联的权重数组。a中的每个值都根据其关联的权重对平均值做出贡献。权重数组可以是一维的(在这种情况下，它的长度必须是沿给
avg = sum(a * weights) / sum(weights)        
"""
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
#print(a)
#print('行最大值', np.amax(a, axis=1))
#print('列最大值', np.amax(a, axis=0))
#print('行最小值', np.amin(a, axis=1))
#print('列最小值', np.amin(a, axis=0))
#print('最大-最小', np.ptp(a))
#print('行最大-最小', np.ptp(a, axis=1))
#print('列最大-最小', np.ptp(a, axis=0))

# 50%的分位数， a排序后的中位数
#print('百分值', np.percentile(a, 50))
#print('行百分值', np.percentile(a, 50, axis=1))
#print('列百分值', np.percentile(a, 50, axis=0))

# 中位数
#print('中位数', np.median(a))
#print('行位数', np.median(a, axis=1))
#print('列位数', np.median(a, axis=0))

# 平均值
#print('平均值', np.mean(a))
#print('行平均值', np.mean(a, axis=1))
#print('列平均值', np.mean(a, axis=0))

# 方差
b = np.array([1, 2, 3, 4])
print(b)
#print('方差', np.var(b))
#print('标准差', np.std(b))

#  加权平均值
c = np.array([20, 30, 50])
print('加权平均值', np.average(c))
print('平均值', np.mean(c))

#x = (80, 90, 95)
#y = (95, 90, 80)
#x1 = np.average(x, weights=[0.2, 0.3, 0.5])
#y1 = np.average(y, weights=[0.2, 0.3, 0.5])
#if x1 > y1:
#    print("小明")
#else:
#    print("小刚 ")


"""

"""



"""
vdot 向量点积
      二维，计算两个数组所有对应下标元素成绩的和
      1*11 + 2*12 + 3*13 + 4*14
"""
q = np.array([[1, 2], [3, 4]])
w = np.array([[11, 12], [13, 14]])
#print(q, w)
#print('向量点积', np.vdot(q, w))

"""
inner 向量内积
      一维，向量内积 1*0 + 2*1 + 3*10
      二维，返回最后一个
"""
e = np.array([1, 2, 3])
r = np.array([0, 1, 0])
print('向量内积', np.inner(e, r))

t = np.array([[1, 2], [3, 4]])
y = np.array([[11, 12], [13, 14]])
print('向量内积', np.inner(t, y))


"""

"""
