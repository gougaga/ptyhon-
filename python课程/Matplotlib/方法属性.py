from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']
# x轴
times = ['2015/8/1', '2015/10/12', '2015/12/23', '2016/3/4', '2016/5/15', '2016/7/26', '2016/10/6', '2016/12/17']
print('时间', times)
# y轴（收入）
income = np.random.randint(500, 2000, size=len(times))
# y轴（支出）
expense = np.random.randint(300, 1500, size=len(times))
print('金额', expense)
# 设置表头/名字：（图像，x轴， y轴）
plt.title('收入支出图')
# x轴
plt.xlabel('日期')
# y轴
plt.ylabel('金额')
# 绘制图形
plt.xticks(range(len(times)), rotation=45)
plt.plot(times, income, label='收入')
plt.plot(times, expense, label='支出')
# 图例 默认使用 绘图中的label参数
plt.legend(loc='upper right')   # 图例在上右方
# zip方法：按照位置信息对列表数据一一对应
for a, b in zip(times, income):
    plt.text(a, b, '%s万' % b)
for q, w in zip(times, expense):
    plt.text(q, w, '%s万' % w)
plt.show()