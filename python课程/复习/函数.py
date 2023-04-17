def sca(a, b):
    x = a + b
    print(x)
sca(11, 3)

def b():
    a = int(input('输入数值'))
    b = int(input('输入数值'))
    c = a + b
    print(c)
def c():
    li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    a = input('输入数值')
    b = input('输入第二个数值')
    if a in li and b in li:
        return int(a) + int(b)
    else:
        return a + b

print(c())

# 函数调用嵌套调用执行顺序

# 示例
# 自定义函数testB
def testB():
    print('------- testB start --------')
    print('这里是testB函数执行的代码....（省略）....')
    print(' ---------testB end ---------')
# 自定义函数testA
def testA():
    print('------testA start --------')
    testB()
    print('-----testA end--------')
testA()

# 函数嵌套调用执行流顺序
'''
1. 自定义函数只有在函数被调用时，函数才会执行
2.如果函数A中，调用了另一个函数B，那么先把函数B中的任务都执行完毕之后才会回到上次函数A执行的位置
'''