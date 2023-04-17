import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

#
labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其他']
x = [200, 500, 1200, 7000, 200, 900]
plt.title('家庭支出')
explode = (0.03, 0.05, 0.06, 0.04, 0.08, 0.21)
plt.pie(x, labels=labels, autopct='%.2f%%', pctdistance=1.3, labeldistance=1.5)
plt.show()