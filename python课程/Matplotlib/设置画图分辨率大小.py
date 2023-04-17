from matplotlib import pyplot as plt
import numpy as np
# 大小
plt.rcParams['figure.figsize'] = (5, 3)
#plt.plot()
# 分辨率
plt.rcParams['figure.dpi'] = 100
#x = np.arange(-10, 11)
#y = x ** 2
#plt.plot(x, y)

#q = np.arange(0, 100, 10)
#w = q ** 2
# linewidth= 线条粗细; color= 线条颜色; alpha= 透明度
#plt.plot(q, w, color='r', linewidth=5, linestyle='-.', marker='x', alpha=0.7)
# 颜色  标记  样式
#plt.plot([1, 2, 3], [4, 7, 6], 'r*--')
#plt.plot([2, 4, 5], [1, 8, 7], 'm+--')

# 中文 负号， 大小， 分辨率
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 创建图像对象
#fig = plt.figure('f1', figsize=(6, 4), dpi=70)
#plt.plot()
#r = np.arange(0, 50)
#t = r ** 2
# 创建图形对象， 设置参数
#plt.figure('f1', figsize=(4, 2), dpi=100, facecolor='')
#plt.plot(r, t)
figg = plt.figure(figsize=(4, 2), facecolor='r')
# 从画布起始位置绘制，宽高和画布相同
axesl = figg.add_axes([0, 0, 1, 1])
# 画布20%开始绘制 宽高是画布的50%
axes2 = figg.add_axes([0, 2, 0, 2, 0, 5, 0, 5])
print(axesl)
plt.show()