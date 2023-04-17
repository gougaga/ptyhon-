from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

# 指定分组个数
bins = 10
fig, ax = plt.subplots()
# 分别生成 1000， 5000，2000个数字
x_values = [np.random.random(n) for n in [10000, 5000, 2000]]
ax.hist(x_values, bins=bins, label=list('ABC'))
ax.legend()
plt.show()

x1 = np.random.randint(140, 180, 200)
x2 = np.random.randint(140, 180, 200)
plt.hist([x1, x2], bins=10, stacked=True,  edgecolor='white')
plt.show()