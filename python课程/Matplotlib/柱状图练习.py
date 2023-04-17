import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

# x 轴 国家
countries = ['千与千寻', '玩具总动员4', '黑衣人', '全球追击', '阿斯顿']
# 第一天
gold_medal = np.array([4053, 7548, 6543])
# 第二天
silver_medal = np.array([1840, 4013, 3412])
# 第三天
bronze_medal = np.array([2080, 1673, 2342])
width = 0.2
# 将x轴转化为数值
q = np.arange(len(countries))
# 确定x轴起始位置
gold_x = q
silver_x = q + width
bronze_x = q + 2 * width
# 绘图
plt.bar(gold_x, gold_medal, color='gold', width=width, label='第一天')
plt.bar(silver_x, silver_medal, color='silver', width=width, label='第二天')
plt.bar(bronze_x, bronze_medal, color='brown', width=width, label='第三天')

# 把x轴转化为国家
plt.xticks(q + width, labels=countries)
plt.legend(loc='upper right')
plt.show()
# 直接显示文本信息， 奖牌数量
for i in range(len(countries)):
    plt.text(gold_x[i], gold_medal[i], gold_medal[i], va='bottom', ha='center', fontsize=8)
    plt.text(silver_medal[i], silver_medal[i], silver_medal[i], va='bottom', ha='center', fontsize=8)
    plt.text(bronze_x[i], bronze_medal[i], bronze_medal[i], va='bottom', ha='center', fontsize=8)