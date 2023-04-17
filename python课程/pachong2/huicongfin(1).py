import requests
from lxml import html
import csv

class Huicong(object):
    def __init__(self):
        self.url = 'https://www.hc360.com/'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

    # 得到类目信息
    def cate(self):
        with open('hhhhhccc.csv', 'a+', newline='')as f:
            obj = csv.writer(f)
            obj.writerow(['一级类目', '二级类目', '三级类目', '名字', '价格', '图片'])
        response = requests.get(self.url, headers=self.header)
        response.encoding = 'utf-8'
        page = html.etree.HTML(response.text)
        cate_li = page.xpath('//dd[@class="aside-dd"]/dl')
        for item in cate_li:
            cate1 = item.xpath('.//dt[@class="sub-menu-dt"]/span/text()')  # 一级类目
            cate2_li = item.xpath('.//dd[@class="sub-menu-dd"]/dl')
            for i in cate2_li:
                cate2 = i.xpath('.//dt/text()')  # 二级类目
                cate3_li = i.xpath('.//dd/a')  # 三级类目列表
                for j in cate3_li:
                    cate3 = j.xpath('.//text()')
                    cate3_link = j.xpath('.//@href')
                    link = 'https://www.hc360.com/' + str(cate3_link[0])
                    good = self.goods(link, cate1, cate2, cate3)
                    print(good)
        pass
    def goods(self, url, c1, c2, c3):
        response = requests.get(url, headers=self.header)
        response.encoding = 'utf-8'
        # 解析
        info = html.etree.HTML(response.text)
        li_goods = info.xpath('//div[@class="wrap-grid"]/ul/li')
        for item in li_goods:
            good = {}
            name = item.xpath('.//dd[@class="newName"]/a/@title')  # 名字
            if len(name) > 0:
                good['name'] = name[0]
            else:
                good['name'] = ''
            price = item.xpath('.//span[@class="seaNewPrice"]/text()')  # 价格
            if len(price) > 0:
                good['price'] = price[1].replace('\r\n', '')
            else:
                good['price'] = '0'
            img = item.xpath('.//a[@class="nImgBox title"]/img/@src')
            if len(img) > 0:
                a = img[0].replace('../', 'https://www.hc360.com/')

                good['img'] = a
            else:
                good['img'] = ''
            good['cate1'] = c1
            good['cate2'] = c2
            good['cate3'] = c3
            return good
        open('hhhhhccc.csv', 'a+')
        pass
hui = Huicong()
hui.cate()
