import numpy as np
# 操作文件 loadtxt（fname， dtype = float_，conments='#', deimiter = None,converters = None)

# 读取txt文件
data = np.loadtxt('has_title.txt', encoding='utf-8', dtype='str_')
#print(data)

data1 = np.loadtxt('data1.txt', dtype='int_')
#print(data1)



# 读取csv文件
data2 = np.loadtxt('wb.csv', dtype=np.str_, delimiter=',')
print(data2[1])
print(data.shape)

# 数据读取 has_title.txt
a = np.loadtxt('has_title.txt', encoding='utf-8', dtype=np.str_)
print('原表格：', a)
# 当文档不同内容需要不同数据类型时，需要自定义类型
dt = np.dtype([('name', 'U3'), ('age', 'i1'), ('gender', np.str_, 1), ('height', 'i2')])
data3 = np.loadtxt('has_title.txt', dtype=dt, skiprows=1, encoding='utf-8')
print('修改数据类型：', data3)
print('年龄中位数', np.median(data3['age']))
print('身高中位数', np.median(data3['height']))
# 求平均身高
print('身高平均数', np.mean(data3['height']))
# 计算女生平均身高
isgirl = data3['gender'] == "女"
print(isgirl)
print(data3['height'])
print(data3['height'][isgirl])

def parse_data(num):
    if num:
        return int(num)
    else:
        return 0
# 再来读取
# 自定义数据类型
dt = np.dtype([('age', 'i1'), ('height', 'i2')])
print(dt)
stu = np.loadtxt('has_empty_data.csv', dtype=dt, skiprows=1, delimiter=',', usecols=(1, 3), converters={1: parse_data, 3: parse_data})
print(stu)
print(stu['age'], stu['age'].dtype)
# 求年龄平均值
print('年龄平均值', np.mean(stu['age']))
# 根据现实情况，学生年龄不会为0，为了减小误差，可以 用中位数代替
# 中位数
ages = stu['age']
ages[ages == 0] = np.median(ages)
print(ages)
print('转化后平均年龄', '{:.2f}'.format(np.mean(ages)))