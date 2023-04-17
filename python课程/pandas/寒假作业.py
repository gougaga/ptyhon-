import pandas as pd
import numpy as np
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
# 中文设置
plt.rcParams['font.sans-serif'] = ['FangSong']

ar1 = np.array(np.arange(30))
aee = ar1.reshape(6, 5)
ar1.resize(5, 6)
print(ar1)
print('-------------')
print(aee)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('------提取出数组中所有奇数  -------')
print(x[x % 2 == 1])
x[x % 2 == 1] = -1
print('------修改奇数值修改为-1-------')
print(x)

t = np.random.randint(10, 49, size=10)
print(t)
t1 = t[::-1]
print('-----创建一个从10到49的ndarray对象,并进行倒序复制给另一个变量--------')
print(t1)

s = np.random.randint(0, 100, size=5)
print('-------4. 使用随机函数，在0-100 之间随机生成一个一维数组有5个元素------')
print(s)

a = [[1, 2, 3], [4, 5, 6]]
print('-------如何把数组 a= [[1,2,3],[4,5,6]] 变成数组 a1=[[1,2,3],[4,5,6],[7,8,9]]------')
print(np.append(a, [[7, 8, 9]], axis=0))

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x)
arr = np.delete(x, 2, axis=0)
print('----删除数组第三列---------')
print(arr)
arr1 = np.delete(x, 2, axis=1)
print('---.删除数组第三行----------')
print(arr1)

# x 轴 电影

pf = ['想见你', '阿凡达：水之道', '绝望支付']
y1 = np.array([4053, 7548, 6543])
y2 = np.array([1840, 4013, 3421])
y3 = np.array([2080, 1673, 2342])
width = 0.2
plt.figure(figsize=(20, 8), dpi=80)
x1 = list(range(len(pf)))
x2 = [i + width for i in x1]
x3 = [i + 2 * width for i in x1]
plt.bar(range(len(pf)), y1, width=width, color='gold', label='想见你')
plt.bar(x2, y2, width=width, color='orange', label='阿凡达：水之道')
plt.bar(x3, y3, width=width, color='yellow', label='绝望支付')
plt.xticks(x2, pf, fontsize=20)
plt.yticks(range(0, 8000, 1000), fontsize=20)
plt.title("票房统计", fontsize=20)
plt.ylabel("票数", fontsize=20)
plt.xlabel("电影名", fontsize=20)
plt.rc('legend', fontsize=18)
plt.legend(loc="upper right")
for i in range(len(a)):
        plt.text(x1[i], y1[i], y1[i], va='bottom', ha='center')
        plt.text(x2[i], y2[i], y2[i], va='bottom', ha='center')
        plt.text(x3[i], y3[i], y3[i], va='bottom', ha='center')
plt.show()

a = ["想见你", "阿凡达：水之道", "绝望主夫"]
one = np.array([3100, 5878, 5500])
two = np.array([4000, 6795, 5678])
three = np.array([3560, 4599, 5600])
width = 0.2
plt.title("票房统计")
plt.bar(a, one, color="yellow", label='第一天', bottom=two+three, width=width)
plt.bar(a, two, color="darkorange", label="第二天", bottom=three, width=width)
plt.bar(a, three, color="lightpink", label="第三天", width=width)
plt.ylabel('票数')
plt.legend(loc="upper right")
plt.legend()
for i in range(len(a)):
    b = one[i]+two[i]+three[i]
    plt.text(a[i], b, b, va="bottom", ha="center")
plt.show()

plt.rcParams['figure.figsize'] = (5, 5)
labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其他']
x = [200, 500, 1200, 7000, 200, 900]
plt.title('饼图示例-8月份家庭支出')
plt.pie(x, labels=labels, autopct='%.2f%%')
plt.show()