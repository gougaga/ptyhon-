from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

plt.rcParams['figure.figsize'] = (5, 5)

# 定义标签
labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其他']
# 定义每个标签所占数量
x = [200, 500, 1200, 7000, 200, 900]
plt.title('家庭支出')
# 绘图
# autopct="%.2f%%" 显示百分比保留两位小数
# explode=explode 饼状图分离
explode = (0.03, 0.05, 0.06, 0.04, 0.08, 0.21)
plt.pie(x, labels=labels, autopct="%.2f%%", pctdistance=1.3, labeldistance=1.5)
plt.show()