import requests

#1.请求地址
import requests
import json
from lxml import html
url = 'http://detail.91jf.com/index/category_goods_list?category_id=102'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
page = html.etree.HTML(res.text)
cate1 = page.xpath("//div[@class='pro_list_div g-clearfix c']/ul/li")
for item in cate1:
    t = item.xpath('.//div/a/img/@src')
    s = item.xpath('.//div/b/text()')
    j = item.xpath('.//div[@class="row row-2 title"]/a/@title')
    g = item.xpath('.//div/a[@class="c7 fl"]/text()')
    d = item.xpath('.//div[@class="location"]/span[@class="c7"]/text()')
    print(t[0])
    print(s[0])
    print(j[0])
    print(g[0])
    print(d[0])

import scrapy