import requests
import json
import re
#1.请求地址
#2.请求头
#3.请求网页
#4.获取响应文本信息
#5.使用正则或者字符串方法得到想要数据
#6.使用json模块
#7.字典取值拿到想要信息
#8.存储

#1.请求地址
url = 'https://you.163.com/item/list?categoryId=1005002&_stat_area=nav_5&_stat_referer=index'
#2.请求头
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
#3.请求网页
res = requests.get(url,headers = header)
#指定编码格式
res.encoding = 'utf-8'
#4.获取响应文本信息
page = res.text
# print(page)
#5.使用正则或者字符串方法得到想要数据
# li = re.findall('var json_Data=(.*)};',page)
# info = li[0]+'}'
#使用字符串方法获取想要数据
info = page.split('var json_Data=')[1].split('json_Data.currentTimestamp')[0]
info = info.replace('};','}')
print(info)
#6.使用json模块
data = json.loads(info)
#7.字典取值拿到想要信息
categoryItemList = data['categoryItemList']
for item in categoryItemList:
    itemList = item['itemList']
    for itl in itemList:
        name = itl['name']
        simpleDesc = itl['simpleDesc']
        retailPrice = itl['retailPrice']
        scenePicUrl = itl['scenePicUrl']+'?type=webp&quality=95&imageView'
        print(name,simpleDesc,retailPrice,scenePicUrl)
#     pass