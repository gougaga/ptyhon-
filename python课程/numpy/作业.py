import numpy as np
"""
创建一个20个元素得数组，分别改变成两个形状：（4，5），（5，6） （提示：超出范围用resise）
"""
a = np.arange(20).reshape(4, 5)
b = np.resize(a, (5, 6))
print('b', b)
print('a', a)
"""
创建一个（4，4）得数组，把其他元素类型给位字符类型
"""
c = np.arange(16).reshape(4, 4)

# astype()
c = c.astype('str_')
print('c', c)
"""
x = np.array([[0,1,2], 3, ,5],[6,7,8],[9,10,11])
1.提出数组中所有奇数
2.修改奇数值为-1
"""
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('j', x[x % 2 == 1])  # 奇数
print('o', x[x % 2 == 0])  # 偶数
print('8', x[x > 8])
x[x % 2 == 1] = -1
print('3:', x)
"""
1.创建0到24得5*5数组ar，通过索引，其ar[4]、ar[:2,3:]、ar[3][2]分别是多少
2.创建0到9得2*5数组ar，筛选出元素大于5得值并生成新的数组
3.创建一个二维数组10*10数组，使该数组边界值为1，内部值为0
4.创建一个从10到49得nadarray对象，并进行倒叙赋值给另一个变量
5.a=np.arrange（0，20）.reshape（4，5），需要更换第二行和第三行得位置
6.分别反转练习5中二维数组得列，行
"""
ar1 = np.arange(25).reshape((5, 5))
print('原数组', ar1)
print('1:', ar1[4])
print('1.1:', ar1[:2, 3:])
print('1.2:', ar1[3][2])

ar2 = np.arange(10).reshape((2, 5))
print('原数组', ar2)
print('5:', ar2[ar2 > 5])
"""

"""