from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

# x轴数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# y 轴数据
y = np.array([1, 4, 9, 16, 25, 36, 49, 64])
s = (20 * np.random.randn(8)) ** 2
# 绘图
plt.scatter(x, y, s=s)
plt.show()

# 自定义点的颜色和透明度
# s=s  表示点的面积
# c=colors 表示点的颜色
x1 = np.random.rand(50)
y1 = np.random.rand(50)
# 点的面积随机
s1 = (10 * np.random.rand(50) ** 2)
# 颜色随机
colors = np.random.rand(50)
# 绘图
plt.scatter(x1, y1, s=s1, c=colors)
plt.show()