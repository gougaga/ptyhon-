import requests
from lxml import html
start_url = 'https://ke.qq.com/'
url = 'https://ke.qq.com/course/list?mt=1001&st=2064'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
#请求地址
response = requests.get(url, headers=header)
#指定响应编码格式
response.encoding = 'utf-8'
#文档树对象
page = html.etree.HTML(response.text)
#使用xpath进行解析
div_li = page.xpath('//li/a[@rel="nofollow"]/text()')

for item in div_li:
    name = item.xpath('.//h3[@class="kc-course-card-name"]/@title')
    link = item.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href')
    if len(name) > 0:
        name = name[0]
    else:
        name = ''
    if len(link) > 0:
        link = start_url+link[0]
    else:
        link = ''
    print(name,link)
