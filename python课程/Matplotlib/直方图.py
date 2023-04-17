from matplotlib import pyplot as plt
import numpy as np
# 负数设置（中文）
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

# 使用 numpy 随机生成 300个数字
x_value = np.random.randint(140, 180, 300)
plt.hist(x_value, bins=10, edgecolor='white')
plt.title('数据统计')
plt.xlabel('身高')
plt.ylabel('比率')
plt.show()

num, bins_limit, patches = plt.hist(x_value, bins=10, edgecolor='red')
plt.grid(ls='--')
print(num)
print(bins_limit)
print(patches)
plt.show()
for i in patches:
    print(i)

xx_value = np.random.randint(160, 190, 300)
# 添加图名
plt.title('身高图')
plt.xlabel('身高')
# 绘制直方图  ----有返回值
numm, binss_limt, patchess = plt.hist(xx_value, bins=10, edgecolor='white')
print('num 是分组区间对应的频率', numm, end='\n \n')
print('binss_limt 是分组时的分隔值', binss_limt, end='\n \n')
print('patchess 是 直方图的列表对象', type(patchess), end='\n \n')
x_li = []
he_li = []
for i in patchess:
    print(i)
    x_li.append(i.get_x())
    he_li.append(i.get_height())
print(x_li)
print(he_li)
plt.xticks(binss_limt, rotation=45)   # 数值显示在正确的位置
plt.show()

xxx_value = np.random.randint(160, 190, 300)

# 创建画布
fig, ax = plt.subplots()
nummm, binsss_limit, patchesss = plt.hist(xxx_value, bins=10, edgecolor='r')
print(nummm)
# num 的数量是10， binsss_limit 是11， 需要截取
print(binsss_limit[:-1])
# 曲线图
ax.plot(binsss_limit[:10], nummm, '--', marker='o')
plt.xticks(binsss_limit, rotation=45)
plt.show()