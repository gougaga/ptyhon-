from matplotlib import pyplot as plt
import numpy as np

a = np.arange(-50, 51)
y = a ** 2
print(y)
print(a)
plt.plot(a, y)
plt.show()

# 设置中文之后，负数符号不显示了
plt.rcParams['axes.unicode_minus'] = False  # 修改轴中得负号编号
plt.rcParams['font.sans-serif'] = ['FangSong']  # 中文设置
# 设置中文之后，负数符号不显示了
x = np.arange(-100, 100)
i = x + 1
plt.title("函数图")
plt.plot(x, i)
plt.show()
# plt.rcParams['font.sans-serif'] = ['FangSong']设置中文
# 设置负数 plt.rcParams['axes.unicode_minus'] = False

# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
# 创建b为 -10 到10 得整数
b = np.arange(-10, 11)
c = b ** 2
# 设置标题
plt.title('y=x**2，x的取值范围是[-10, 10]')
# 设置x轴（b），y轴（c）名称
plt.xlabel('x轴')
plt.ylabel('y轴')
# 绘图
plt.plot(b, c)
plt.show()



# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
r = np.arange(5, 15)
y = 1/r
y1 = y - r
# 设置标题
plt.title('y=1/x,x的取值范围时[5, 15]', fontsize=12)
# 设置x轴y轴
plt.xlabel('x轴', fontsize=12)
plt.ylabel('y轴')

plt.polar(r, y, linewidth=10)
plt.polar(r, y1)
plt.show()
# fontsize=12 设置字体的大小


# 日期
times = np.arange(1990, 2020).astype(np.str_)
# 销量
sales = np.random.randint(500, 2000, size=len(times))
# 绘图
# plt.xticks(range(0, len(times)), ['%s年' %i for i in times], rotation=45)
plt.xticks(range(0, len(times), 2), rotation=45)
plt.plot(times, sales)
plt.show()