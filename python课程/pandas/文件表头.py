#-*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

'''
header：用作列名的行号，以及数据的开头。默认行为是推断列名：如果没有传递任何名称，则该行为与header=0相同，并且从文件的第一行推断列名，如果显式传递列名，则该行为与header=None相同。显式传递header=0以替换现有名称。标题可以是整数列表，指定列上多索引的行位置，例如[0，1，3]。未指定的中间行将被跳过(例如，本例中跳过2行)。请注意，如果skip_blank_lines=True，此参数将忽略注释行和空行，因此header=0表示数据的第一行，而不是文件的第一行。
names:当names没被赋值时，header会变成0，即选取数据文件的第一行作为列名；当names被赋值，header没被赋值时，那么header会变成None。如果都赋值，就会实现两个参数的组合功能。
'''

# naems没有赋值，header被赋值
# 默认header=0 会选取文件第一行作为列名（表头）
# header=1 选取第2行作为表头(行索引从0开始）第2行下面是数据
df = pd.read_csv('students2.csv', encoding='gbk', header=2)
print(df)

# header=None,给自己指定的表头（自定义）
df1 = pd.read_csv('students2.csv',
                  encoding='gbk',
                  names=['编号', '姓名', '地址', '性别', '出生日期'])
print('--------------------------header=None,给自己指定的表头（自定义）--------------------------------------')
print(df1)
'''可以看到，names适用于没有表头的情况，指定names没有指定header，那么header相当于None。一般来说，读取文件的时候会有一个表头，一般默认是第一行，但是有的文件中是没有表头的，那么这个时候就可以通过names手动指定、或者生成表头，而文件里面的数据则全部是内容。所以这里id、name、address、date也当成是一条记录了，本来它是表头的，但是我们指定了names，所以它就变成数据了，表头是我们在names里面指定的。'''

# name和header都被赋值
df2 = pd.read_csv('students2.csv',
                  encoding='gbk',
                  names=['编号', '姓名', '地址', '性别', '出生日期'],
                  header=0)
print('--------------------------name和header都被赋值--------------------------------------')
print(df2)

'''这个时候，相当于先不看names，只看header，header为0代表先把第一行当做表头，下面的当成数据；然后再把表头用names给替换掉。
所以names和header的使用场景主要如下：
1.csv文件有表头并且是第一行，那么names和header都无需指定；
②.csv文件有表头、但表头不是第一行，可能从下面几行开始才是真正的表头和数据，这个时候指定header即可；
③.csv文件没有表头，全部是纯数据，那么我们可以通过names手动生成表头；
4.csv文件有表头、但是这个表头你不想用，这个时候同时指定names和header。先用header选出表头和数据，然后再用names将表头替换掉，就等价于将数据读取进来之后再对列名进行rename;'''


# 4.index_col:我们在读取文件之后所得到的DataFrame的默认索引是0,1,2......., 我们可以通过set_index设定索引，但是也可以在读取的时候就某列为索引

df3 = pd.read_csv('students2.csv', encoding='gbk')
print(df3)

# 要把birthday当作索引
df3 = pd.read_csv('students2.csv', encoding='gbk', index_col='birthday')
print('--------------------------要把birthday当作索引--------------------------------------')
print(df3)

# 时间类型转化pd.to_datetime（）
df3.index
df3.index = pd.to_datetime(df3.index)
print('--------------------------时间类型转化--------------------------------------')
print(df3.index)
#print(df3['2003-10'])
print(df3.loc['2002-2-12'])


# 要把birthday和gender当作索引
df3 = pd.read_csv('students2.csv', encoding='gbk', index_col=['gender', 'birthday'])
print('--------------------------要把birthday和gender当作索引--------------------------------------')
print(df3)

print(df3.loc['男', '2002/6/12'])

# 排序
df3.sort_index(inplace=True)
print('-----排序---------------')
print(df3)

# 只读取文件的某几列
'''5.usecols:返回列的子集。如果是类似列表的，则所有元素都必须是位置性的(即文档歹中的整数索引)，或者是与用户在名称中提供的列名或从文档标题行推断的列名相对应的字符串。如果给出了名称，则不考虑文档标题行
'''
aas = pd.read_csv('students2.csv', encoding='gbk')
print(aas)
aas1 = pd.read_csv('students2.csv', encoding='gbk', usecols=['name', 'gender'])
print('----------只读取文件某几列--------')
print(aas1)

#
'''2.dtype:在读取数据的时候，设定字段的类型。比如，公司员工的id一般是：00001234，如果默认读取的时候，会显示为1234，所以这个时候要把他转为字符串类型，才能正常显示为00001234：'''
df4 = pd.read_csv('students2.csv', encoding='gbk', dtype={'id': int, 'name': str})
# 设置数据类型为str，dtype 会以object显示
print(df4)
print('--------数据类型-----------')
print(df4['id'])
print(df4['name'])
