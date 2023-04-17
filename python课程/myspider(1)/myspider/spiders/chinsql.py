# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

#将数据存储到mysql数据库中
# 1.修改爬虫文件（就是对 parse 方法的修改）----和items文件联系
# 2.修改settings文件
# 3.修改管道文件pipelines(和数据库操作文件连接)
# 4.新增加一个操作数据库的文件

class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['chinaz.com']
    start_urls = ['https://top.chinaz.com/hangye/']
    def parse(self, response):
        #response是我们的响应
        info = response.xpath('//ul[@class="listCentent"]/li')
        for ite in info:
            ##将得到的数据封装到一个MyspiderItem 对象
            items = MyspiderItem()
            # response.xpath()得到的数据类型<class 'scrapy.selector.unified.SelectorList'>
            # extract()返回列表  extract_first()返回列表值[就是取第一个]
            # name = ite.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract()[0]# 名称
            data = {}
            name = ite.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract_first() # 名称
            info = ite.xpath('.//p[@class="RtCInfo"]/text()').extract_first() # 简介
            rank = ite.xpath('.//strong[@class="col-red02"]/text()').extract_first()  # 排名
            # print(name,info,rank)

            items['name'] = name
            items['info'] = info
            items['rank'] = rank
            yield items

        pass