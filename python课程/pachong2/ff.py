import re

str1 = "速度与激情10"
ret = re.match(r"速度与激情\d", str1)
str2 = 'qweerafag'
ret2 = re.search(r'qwe', str2)
print(ret2.group())
print(ret.group())
ret3 = re.findall(r"qwe", str2)
print(ret3)

strs='阅读数为9999，点赞量为100'
a = re.findall('\d', strs)
b = re.findall('\d+', strs)
#print(a)
print(b[1])

# flag：
# 1. 知道正则三个匹配方法，以及区别
# 2.理解\d和\d+

# *：0个或者无数个
# +：匹配1次过无数个
# ？：匹配1个或0个
# .（）：匹配任意字符


# 3.会使用re.findall（）  返回的是列表

# 4.理解贪婪模式与非贪婪模式
# 贪婪模式(.*)  非贪婪模式(.*?)

info = '[速度与激情10速度与激情10速度与激情10速度与激情10]'
reg = '\[.*?与'
res = re.findall(reg, info)
print(res)