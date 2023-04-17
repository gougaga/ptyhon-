# -*-coding: UTF-8 -*-
# 导入time模块
import time
# 生成timestamp
print(time.time())
print(int(time.time()))
# 程序开始时间
start_time = time.time()
# 程序
s = ""
for i in range(10000):
     s += str(i)
end_time = time.time()
print("程序消耗时间=",end_time-start_time)
#生成struct_time
# timestamp to struct_time 本地时间
my_time = time.localtime()
print(my_time)
print(my_time.tm_year)
print(my_time.tm_mon)
print(my_time.tm_mday)
# 将timsstamp转化为 struct_time
print(time.localtime(1650177058))
#格式化字符串到 struct_time
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))
print(time.mktime(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')))
#生成format_time
#struct_time to format_time
print(time.strftime("%Y-%m-%d %X"))
print(time.strftime("%Y-%m-%d %X",time.localtime()))
#生成format_time
#struct_time to format_time
print(time.strftime("%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %X",time.localtime()))
#生成format_time
#struct_time to format_time
print(time.strftime("%m-%d-%Y"))
print(time.strftime("%Y-%m-%d %X",time.localtime()))
# struct_time元组元素结构
"""
属性 值
tm_year（年） 比如2011
tm_mon（月） 1 - 12
tm_mday（日） 1 - 31
tm_hour（时） 0 - 23
tm_min（分） 0 - 59
tm_sec（秒） 0 - 61
tm_wday（weekday） 0 - 6（0表示周日）
tm_yday（一年中的第几天） 1 - 366
tm_isdst（是否是夏令时） 默认为-1
作用:
取得 时间戳/时间格式的字符串 中对应的 年/月/日等信息
作为时间戳和字符串时间之间的桥梁
"""
time_stuct = time.strptime('2011-05-07 16:37:06', '%Y-%m-%d %X')
print(time_stuct.tm_year)
print(time_stuct.tm_mon)
print(time_stuct.tm_mday)
print(time_stuct.tm_hour)
print(time_stuct.tm_min)
my = 'aaa'
'%s'% my
my_int = 1
'%d'% my_int
"我们在{}工作".format('家里')
addr = "家里"
f"我们在{addr}工作"
# format time结构化表示
"""
格式 含义
%Y -年[0001，...，2018，2019，...，9999]
%m -月[01，02，...，11，12]
%d -天[01，02，...，30，31]
%H -小时[00，01，...，22，23
%M -分钟[00，01，...，58，59]
%S -秒[00，01，...，58，61]
%X 本地相应时间
%y 去掉世纪的年份（00 - 99）
"""
#常见结构化时间组合
print(time.strftime("%Y-%m-%d %X"))
print( time.strftime("%Y-%m-%d"))
print( time.strftime("%m"))
# time运算
#获取明天的这个时间点
t1 = time.time()
#timestamp加减单位以秒为单位
t2=t1+24*60*60
print(time.strftime("%Y-%m-%d %X",time.localtime(t2)))
# 倒计时
for i in range(5):
    print('\r',' %s 秒！' % (5-i), end='')
    # 暂停1s后运行
    time.sleep(1)
print('\r',"发射!!!!")










