# 导包
import pandas as pd
# 2.文件路径
# df = pd.read_csv(r"C:\Users\杨佳音\Desktop\AI2班课件\2022年12月\my_csv.csv")
# print(df)
# 3.相对路径
df = pd.read_csv('./my_csv.csv')
print(df)
df2 = pd.read_csv(r"C:\Users\杨佳音\Desktop\AI2班课件\2022年12月\students2.csv", encoding='gbk')
print(df2)
# df1 = pd.read_csv('./students2.csv', encoding='gbk')
# print(df1)
# 文件对象
f = open('./students2.csv', encoding='gbk')
pd.read_csv(f)


