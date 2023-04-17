import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']
# 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌
gold_medal = [16, 12, 9, 8, 8]
# 银牌
silver_medal = [8, 10, 4, 10, 5]
# 铜牌
bronze_medal = [13, 5, 2, 7, 5]

# x 轴国家
countries = ['挪威','德国','中国','美国','瑞典']
# 总奖牌数
all_medal = np.array([37,27,15,25,18])
# 金牌个数
gold_medal = np.array([16,12,9,8,8])
# 银牌
silver_medal = np.array([8,10,4,10,5])
# 铜牌
bronze_medal = np.array([13,5,2,7,5])

# 绘制堆叠图
width = 0.4

# 绘制金牌
plt.bar(countries, gold_medal, color='gold', label='金牌', bottom=silver_medal+bronze_medal, width=width)
plt.bar(countries, silver_medal, color='silver', label='银牌', bottom=bronze_medal, width=width)
plt.bar(countries, bronze_medal, color='brown', label='铜牌', width=width)
plt.ylabel('奖牌数')
plt.legend(loc='upper right')

# 设置文本值---奖牌数量
for i in range(len(countries)):
    max_y = gold_medal[i]+silver_medal[i]+bronze_medal[i]
    plt.text(countries[i],max_y,max_y,va='bottom',ha='center')