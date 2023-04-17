# 位置参数：调用函数时根据函数定义的参数位置来传递参数
#  示例：
def user_info(name, age, gender):
    print(f'您的姓名是:{name}, 年龄是:{age}, 性别是:{gender}')
user_info('TOM', 20, '男')
# 注意：传递和定义参数的顺序及个数必须一致
user_info(name='ROse', age=20, gender='女')

def user_info(name, age, gender='男'):
    print(f'您的姓名是:{name}, 年龄是:{age}, 性别是:{gender}')
user_info('ROse', 20, '女')
user_info('TOM', 20)

# 不定长参数：不定长参数也可叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
# 1.
def user_inf(*args):
    print(args)
user_inf('TOM')
user_inf('TOM', 18)

def user_in(**kwargs):
    print(kwargs)
user_in(name='TOM', age=18, id=110)

# lambda
#1.用于改写简单逻辑的功能函数
#2.在def关键字不能出现的地方使用
#	示例：
lst = [lambda x: x**2, lambda x: x**2, lambda x: x**2,]
for f in lst:
    print(f(9))