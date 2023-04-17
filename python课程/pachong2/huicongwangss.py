from lxml import html
import requests
url = "http://www.hc360.com/seller/search5.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=header)
res.encoding = 'utf-8'
info = res.text
print(info)
# 解析
html = html.etree.HTML(info)
li_goods = html.xpath('//div[@class="wrap-grid"]/ul/li')
for item in li_goods:
    good = {}
    name = item.xpath('.//dd[@class="newName"]/a/@title')  # 名字
    price = item.xpath('.//span[@class="seaNewPrice"]/text()')  # 价格
    img = item.xpath('.//a[@class="nImgBox title"]/img//@src')
    good["name"] = name[0]
    good["price"] = price[1]
    print(img[0])
    a = img[0].replace('../', 'https://www.hc360.com/')
    good['img'] = a
    print(good)
    break

# //div[@class="s-mod-main"]   #商品信息
import pymysql
coon = pymysql.connect