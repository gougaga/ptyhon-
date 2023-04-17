import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = [16, 12, 9, 8, 8]
# 银牌个数
silver_medal = [8, 10, 4, 10, 5]
# 铜牌个数
bronze_medal = [13, 5, 2, 7, 5]

plt.barh(countries, width=gold_medal)
plt.show()
plt.barh(countries, width=silver_medal)
plt.show()
plt.barh(countries, width=bronze_medal)
plt.show()

move = ['新蝙蝠侠', '狙击手', '奇迹笨小孩']
real_day1 = np.array([4053, 2548, 1543])
real_day2 = np.array([7840, 4013, 2421])
real_day3 = np.array([8080, 3673, 1342])
# 确定距离
left_day2 = real_day1
left_day3 = real_day1 + real_day2
# 设置高度 height
height = 0.2
# 绘制图形
plt.barh(move, real_day1, height=height, label='第一天')
plt.barh(move, real_day2, left=left_day2, height=height, label='第二天')
plt.barh(move, real_day3, left=left_day3, height=height, label='第三天')
# 图例
plt.legend()
# 显示文本值 计算宽度值和y轴为值
sum_data = real_day1 + real_day2 + real_day3
for i in range(len(move)):
    plt.text(sum_data[i], move[i], sum_data[i], va='center', ha='left')
plt.show()


move = ['新蝙蝠侠', '狙击手', '奇迹笨小孩']
real_day1 = np.array([4053, 2548, 1543])
real_day2 = np.array([7840, 4013, 2421])
real_day3 = np.array([8080, 3673, 1342])
# 转换y轴为数值
num_y = np.arange(len(move))
# 设定高度
height = 0.2
# 计算每一个起始高度
move1_start_y = num_y
move2_start_y = num_y + height
move3_start_y = num_y + 2 * height
# 绘制
plt.barh(move1_start_y, real_day1, height=height)
plt.barh(move2_start_y, real_day2, height=height)
plt.barh(move3_start_y, real_day3, height=height)
# 将y轴转化为原来的
plt.yticks(num_y + height, move)
plt.show()