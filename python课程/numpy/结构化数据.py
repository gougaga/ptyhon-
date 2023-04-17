import numpy as np
# 创建结构化数据类型
dt = np.dtype([('age', 'U2')])
#print(dt)
obj = np.array([('你们'), 234], dtype=dt)
print(obj)
print(obj['age'])
print('数据类型', obj.dtype)


'''
学生 三个特征：姓名 年龄 成绩， 定义结构化数据类型
   str 字段  name
   int 字段 age
   floa 字段 score
'''
# 定义数据类型
dt = np.dtype([('name', np.str_, 3), ('age', 'i1'), ('score', 'f4')])
stu = np.array([('lyy', 12, 11.11), ('wmd', 13, 12.22)], dtype=dt)
print(stu)
print('名字', stu['name'])
print('年龄', stu['age'])
print('成绩', stu['score'])
