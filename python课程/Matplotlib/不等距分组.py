from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']


fig, ax = plt.subplots()
x = np.random.normal(100, 20, 100)  # 正态分布， 均值标准差
bins = [50, 60, 70, 90, 100, 110, 140, 150]
# 绘图
ax.hist(x, bins, color='r', edgecolor='white')
ax.set_title('不等距分组')
plt.show()