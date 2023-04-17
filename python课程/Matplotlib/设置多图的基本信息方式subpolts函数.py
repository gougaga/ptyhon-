import numpy as np
from matplotlib import pyplot as plt

# 第一种方式
plt.subplot(211, title='pic1', xlabel='x axis')
plt.plot(range(50, 70))
plt.subplot(212, title='pic2', xlabel='x axis')
plt.plot(np.arange(12) ** 2)
# 紧凑布局
plt.tight_layout()
#plt.show()

# 第二种方式
plt.subplot(211)
plt.title('ax3')
#plt.xlabel('xax3')
plt.plot(range(50, 70))

plt.subplot(212)
plt.title('ax33')
plt.plot(np.arange(12) ** 2)
plt.tight_layout

# 第三种方式
# 使用返回的区域对象设置 注意区域对象很多方法都是ser_开头
ax4 = plt.subplot(211)
ax4.set_title('ax4')
ax4.plot(range(50, 70))

ax5 = plt.subplot(212)
ax5.set_title('ax5')
ax5.plot(np.arange(12) ** 2)
plt.tight_layout
#plt.show()

# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']
'''
subplots() 函数
'''
# 生成四个空白图
fiig, axes = plt.subplots(2, 2)
# 第一个绘图区域
# 图像位置
axx1 = axes[0][0]
q = np.arange(1, 5)
w = q ** 2
axx1.plot(q, w)
axx1.set_title('平方')

# 第二个绘图区域
# 图像位置
axx2 = axes[0][1]
axx2.plot(q, np.sqrt(q))
axx2.set_title('平方根')

# 第三个绘图区域
# 图像位置
axx3 = axes[1][0]
axx3.plot(q, np.exp(q))
axx3.set_title('指数')

# 第四个绘图区域
# 图像位置
axx4 = axes[1][1]
axx4.plot(q, np.log10(q))
axx4.set_title('对数')
plt.show()

'''
subpolts与subplot实例：
一个画布中两个图，一个是正常图，一个是移动图
'''
x, c = plt.subplots(1, 2)
# 设置画布的大小和分辨率
x.set_figheight(3)  #  73 * 3 大小
x.set_figwidth(8)   # 73 * 8 大小
# 设置背景色
x.set_facecolor('gray')
# 画图区域1------------
t = np.arange(-50, 50)
y = t ** 2
c[0].plot(t, y)

# 画图区域2------------
c[1].spines['top'].set_color('none')  # 去掉上面
c[1].spines['right'].set_color('none')  # 去掉右面
c[1].spines['left'].set_position(('axes', 0.5))  # 移动y轴
c[1].spines['bottom'].set_position(('data', 0.0))  # 移动x轴
c[1].plot(t, y)

'''
绘制特殊图形，多次调用subplot
'''
# 1
plt.subplot(121, facecolor='r')
plt.subplot(222, facecolor='g')
plt.subplot(224, facecolor='b')

# 2
plt.subplot(321, facecolor='r')
plt.subplot(322, facecolor='r')
plt.subplot(323, facecolor='r')
plt.subplot(324, facecolor='r')
plt.subplot(313, facecolor='b')
plt.show()