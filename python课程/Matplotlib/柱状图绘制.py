import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

"""
柱状图的绘制
matplotlib.pyplot.bar(x,height,width:float=0.8,bottom=None,*,align:str=‘center’,data=None,**kwargs)
·x表示x坐标，数据类型为float类型，一般为np.arange()生成的固定步长列表
·height表示柱状图的高度，也就是y坐标值，数据类型为float类型，一般为一个列表，包含生成柱状图的所有y值
·width表示柱状图的宽度，取值在0~1之间，默认值为0.8bottom柱状图的起始位置，也就是y轴的起始坐标，默认值为None
·align柱状图的中心位置，“center”，"lege"边缘，默认值为’center’
•color柱状图颜色，默认为蓝色·alpha透明度，取值在0~1之间，默认值为1label标签，设置后需要调用plt.legend()生成
·edgecolor边框颜色(ec)
•linewidth边框宽度，浮点数或类数组，默认为None(lw)tick_label：柱子的刻度标签，字符串或字符串列表，默认值为None。
linestyle：线条样式(Is)
"""

'''
基本柱状图
'''
# x轴数据
x = range(5)
# y轴数据
data = [5, 20, 15, 25, 10]
# 设置标题
plt.title('设置边缘格式')
# 网格ls （linestyle）
plt.grid(ls='--', alpha=0.5)
# 绘制柱状图 bootm 形状要一致， 每个柱状图都要给
'''
描边-相关的关键字参数为：
--edgecolor或ec
--linestyle或ls
linewidth或lw
'''
# bottom参数：柱状图的起始位置，也就是y轴的其实坐标， 默认值为none.
plt.bar(x, data, bottom=[10, 20, 5, 0, 10], color=['pink', 'yellow', 'green'], ec='r', ls='--', lw=1)  # color= 循环三个颜色
# facecolor='pink'   同样可以设置粉色
'''
color 和 facecolor 区别：
   color可以设置多个颜色 
   facecolor只能设置一个颜色
'''
plt.show()

# x 轴 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = [16, 12, 9, 8, 8]
# 银牌个数
silver_medal = [8, 10, 4, 10, 5]
# 铜牌个数
bronze_medal = [13, 5, 2, 7, 5]
width = 0.2
# 将x轴转化为数值
q = np.arange(len(countries))
# 确定x轴起始位置
gold_x = q
silver_x = q + width
bronze_x = q + 2 * width
# 绘图
plt.bar(gold_x, gold_medal, color='gold', width=width, label='金')
plt.bar(silver_x, silver_medal, color='silver', width=width, label='银')
plt.bar(bronze_x, bronze_medal, color='brown', width=width, label='铜')

# 把x轴转化为国家
plt.xticks(q + width, labels=countries)
plt.legend(loc='upper right')
plt.show()
# 直接显示文本信息， 奖牌数量
for i in range(len(countries)):
    plt.text(gold_x[i], gold_medal[i], gold_medal[i], va='bottom', ha='center', fontsize=8)
    plt.text(silver_medal[i], silver_medal[i], silver_medal[i], va='bottom', ha='center', fontsize=8)
    plt.text(bronze_x[i], bronze_medal[i], bronze_medal[i], va='bottom', ha='center', fontsize=8)

''''''
# x 轴 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = [16, 12, 9, 8, 8]
# 银牌个数
silver_medal = [8, 10, 4, 10, 5]
# 铜牌个数
bronze_medal = [13, 5, 2, 7, 5]
# 总奖牌数
all_medall = [37, 27, 15, 25, 18]
# 设置画布
fig = plt.figure(figsize=(6, 4), dpi=80)
# 将画布分为两行三列
ax1 = fig.add_subplot(211)
ax1.set_title('奖牌榜')
ax1.tick_params(axis='x', rotaion=45)
ax1.bar(countries, all_medall, color='r')
plt.tight_layout()
ax2 = fig.add_subplot(222)
ax2.set_title('金牌榜')
ax2.tick_params(axis='x', rotation=45)
ax2.bar(countries, gold_medal, color='gold')
plt.tight_layout()
ax3 = fig.add_subplot(223)
ax3.set_title('银牌榜')
ax3.tick_params(axis='x', rotation=45)
ax3.bar(countries, silver_medal, color='silver')
plt.tight_layout()
ax4 = fig.add_subplot(224)
ax4.set_title('铜牌帮')
ax4.tick_params(axis='x', rotation=45)
ax4.bar(countries, bronze_medal, color='brown')
plt.tight_layout()
plt.show()