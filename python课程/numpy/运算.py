import numpy as np
'''
舍入函数
around函数  四舍五入  1.数组 2.摄入的小数位：默认0
floor函数 向下取整数
ceil函数  向上取整数
'''
a = np.array([20.3, 30.63, 40.856, 40.2345])
#print(a)
#print('四舍五入', np.around(a))
#print('向下取整数', np.floor(a))
#print('向上取整数', np.ceil(a))

"""
算法函数 数组的加减乘除,数组必须具有相同的形状，符合广播规则
add（）加法
subtract（）减法
multiply（）乘法
divide（）除法
reciprocal（）倒数，元素的倒数  1/4倒数4/1
power()1.底数 2.幂次方
mod（）两数组余数
"""
a = np.arange(9, dtype=np.float64).reshape(3, 3)
b = np.array([10, 10, 10])
#print('add相加', np.add(a, b))
#print('add相加', np.add(a, b))
#print('subtract相减', np.subtract(a, b))
#print('multiply相乘', np.multiply(a, b))
#print('divide相除', np.divide(a, b))

c = np.array([0.25, 1.33, 1, 100])
#print('倒数', np.reciprocal(c))

d = np.array([10, 100, 1000])
print('幂次方', np.power(d, 3))

#两数组余数
num1 = np.array([10, 20, 30])
bum2 = np.array([3, 5, 7])
print('两数组余数', np.mod(num1, bum2))