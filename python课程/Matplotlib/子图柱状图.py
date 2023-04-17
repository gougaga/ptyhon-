import numpy as np
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(4, 2), facecolor='g')
x = np.arange(0, 50, 2)
y = x ** 2
z = x + 1
axes1 = fig.add_axes([0.0, 0.0, 1.0, 1.0])
axes1.set_title('axes1')
axes1.set_xlabel('X axes1')
index = [x[i] for i in range(len(x))]
# print(index)
axes1.set_xticks(index)
axes1.plot(x, y)
plt.show()
axes2 = fig.add_axes([0.6, 0.6, 0.4, 0.4])
axes2.set_title('axes2')
axes2.set_xlabel('X axes2')
axes2.plot(x, z)
y_len = len(range(50, 71))# 21个 x 的取值范围[0-20]y_len
#要知道根据y x是怎吗取值的
y_len = len(range(50, 71))
print([i for i in range(50, 70)])
a = np.linspace(0, y_len-1, y_len)
print(a)
print(np.linspace(0, 11, 12))
plt.plot(np.arange(12)**2)

print(np.linspace(0, 11, 12))  # 从0开始到11结束生成12个元素---等差数列
plt.plot(np.arange(12) ** 2)  # 这个图会被删除（占领）
plt.subplot(211)  # 2行1列 位置1
plt.plot(range(50, 70), marker='o')
plt.grid()
plt.subplot(212)
plt.plot(np.arange(12) ** 2)

# 如果不想被覆盖之前的图，需要先创建画布
plt.plot([1, 2, 3])
figg = plt.figure(figsize=(4, 2))
figg.add_subpolt(111)
plt.plot(range(20))
figg.add_subpolt(211)
plt.plot(range(50, 70))
plt.show()