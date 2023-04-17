import pandas as pd
import numpy as np
# 对齐运算
s1 = pd.Series(np.random.rand(3), index=list('abc'))
print(s1)
print('*******************************************')
s2 = pd.Series(np.random.rand(3), index=list('bad'))
print(s2)
print('***************************************')
print(s1 + s2)

# 删除和添加
s3 = pd.Series(np.random.rand(5), index=list('abcde'))
print(s3)
print('//////////////////////////////////////')
s4 = s3.drop('a', inplace=False)  # 返回删除后的值，原值保持不变,inplace=False默认参数
print(s4)
print('****************************')
print(s3)
#
s3 = pd.Series(np.random.rand(5), index=list('abcde'))
print(s3)
print('//////////////////////////////////////')
s4 = s3.drop('a', inplace=True)  # 返回删除后的值，原值保持不变,inplace=False默认参数
print(s4)
print('****************************')
print(s3)
