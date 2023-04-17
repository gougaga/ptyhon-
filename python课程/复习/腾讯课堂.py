import requests
from lxml import html
import csv
url = "https://ke.qq.com/course/list?mt=1001&st=2064"
headers = {    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
response = requests.get(url=url, headers=headers)
# 打印网页
#print(response.text)
page = html.etree.HTML(response.text)
# 获取页码

page_num = page.xpath('//li@class="rc-pagination-item rc-pagination-item-34"]/a/text()')[0]
# csv文件
with open('腾讯课堂1.csv','a',encoding='utf-8',newline='') as f:
# 创建witer对象
    write = csv.writer(f)
    write.writerow(["课程名称","课程链接"])
    for i in range(1,int(page_num)+1):
        page_url = url+"&page="+str(i)
        res = requests.get(page_url,headers=headers)
        pagel = html.etree.HTML(res.text)
        #
        div = pagel.xpath("//div[@class='course-list']/div")
        for j in div:
            #
            href = j.xpath(".//a/@href")
            link = 'https://ke.qq.com'+href[0]
            #
            title = j.xpath('.//h3[@class="kc-course-card-name"]/text()')[0]
            list1 = [link, title]
            write.writerow(list1)
            print("存入成功")

