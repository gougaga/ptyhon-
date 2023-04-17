from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']
# x 轴 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = np.array([16, 12, 9, 8, 8])
# 银牌个数
silver_medal = np.array([8, 10, 4, 10, 5])
# 铜牌个数
bronze_medal = np.array([13, 5, 2, 7, 5])
# 总奖牌数
all_medall = np.array([37, 27, 15, 25, 18])
# 确定距离
y = gold_medal
q = gold_medal + silver_medal
# 设置高度 height
height = 0.4
plt.barh(countries, gold_medal, height=height, label='金')
plt.barh(countries, silver_medal, left=y, height=height, label='银')
plt.barh(countries, bronze_medal, left=q, height=height, label='铜')
# 图例
plt.legend()
sum_data = silver_medal + gold_medal + bronze_medal
for i in range(len(countries)):
    plt.text(sum_data[i], countries[i], sum_data[i], va='center', ha='left')
plt.show()


# 转换y轴为数值
num_y = np.arange(len(countries))
# 设定高度
height = 0.2
# 计算每一个起始高度
move1_start_y = num_y
move2_start_y = num_y + height
move3_start_y = num_y + 2 * height
# 绘制
plt.barh(move1_start_y, gold_medal, height=height)
plt.barh(move2_start_y, silver_medal, height=height)
plt.barh(move3_start_y, bronze_medal, height=height)
# 将y轴转化为原来的

plt.yticks(num_y + height, countries)
plt.show()
for i in range(len(countries)):
    plt.text(gold_medal[i], move1_start_y[i], gold_medal[i], va='center', ha='left')
    plt.text(silver_medal[i], move2_start_y[i], silver_medal[i], va='center', ha='left')
    plt.text(bronze_medal[i], move3_start_y[i], bronze_medal[i], va='center', ha='left')


