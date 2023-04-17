'//div/a[@class="post-item-title"]/@href'
from lxml import html
import requests
url = 'https://www.cnblogs.com/'
yrl2 = 'https://www.cnblogs.com/sitehome/p/2'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
#请求地址
response = requests.get(url, headers=header)
#指定响应编码格式
response.encoding = 'utf-8'
page = html.etree.HTML(response.text)
li = page.xpath('//article[@class="post-item"]')
for i in li:
    titlr = i .xpath('.//a[@class="post-item-title/text()"]')[0]
    link = i.xpath('.//a[@class="post-item-title/@href"')[0]
    print(titlr, link)



