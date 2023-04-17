import numpy as np

"""
    广播（Broadcasting）
    广播是一种强大的机制，它允许numpy在执行算术运算时使用不同形状的数组
"""
a = np.repeat((3, 4, 5), 5)
#print(a)
#print(type(a))


# a和b  shape相同
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10, 10, 10], [20, 20, 20]])
c = a * b
#print(c)
#print(a.shape, b.shape)

#形状不同
num1 = np.array([[1, 2, 3], [10, 10, 10], [20, 20, 20]])
num2 = np.array([1, 2, 3])
num3 = num1 + num2
#print(num3)
#print(num1 * num2)

"""
  数学函数 包含了大量各种数学运算的函数， 三角函数， 算术函数， 复数处理等
  三角函数 sin（）正弦  cos（）余弦  arctan（）反正切
  反转计算成角度 degrees（sin，cos，tan） 返回 角度值

"""

a = np.array([30, 45, 60])
# 弧度公式： np.pi / 180
sin_num = np.sin(a * np.pi / 180)
cos_num = np.cos(a * np.pi / 180)
tan_num = np.tan(a * np.pi / 180)
print("正弦", sin_num)   # sin30 = 1/2
print("余弦", cos_num)   # cos60 = 1/2
print("正切", tan_num)   # tan45 = 1

sin_ang = np.arcsin(sin_num)   # 反正弦
cos_ang = np.arccos(cos_num)   # 反余弦
tan_ang = np.arctan(tan_num)   # 反正切
print(sin_ang, "反正弦")
print(cos_ang, "反余弦")
print(tan_ang, "反正切")