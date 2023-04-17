# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['chinaz.com']
    # start_urls = ['http://chinaz.com/']
    start_urls = ['https://top.chinaz.com/hangye/']
    def parse(self, response):
        #response是我们的响应
        info = response.xpath('//ul[@class="listCentent"]/li')
        for ite in info:
            # response.xpath()得到的数据类型<class 'scrapy.selector.unified.SelectorList'>
            # extract()返回列表  extract_first()返回列表值[就是取第一个]
            # name = ite.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract()[0]# 名称
            data = {}
            name = ite.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract_first() # 名称
            info = ite.xpath('.//p[@class="RtCInfo"]/text()').extract_first() # 简介
            rank = ite.xpath('.//strong[@class="col-red02"]/text()').extract_first()  # 排名
            print(name,info,rank)

            # 数据的文件存储（csv文件，json文件）
            #1.用到yield 关键词 返回信息
            #2.返回数据为字典格式
            #3.运行命令

            #方式一：yield返回信息
            yield {
                'name':name,
                'info':info,
                'rank':rank
            }
            # #方式二：yield返回信息
            # data['名字'] =name
            # data['简介'] = info
            # data['排名'] = rank
            # yield data

        pass

    for i in range(1,35):
        print(i) # i的取值 1---34
        s = f'https://ke.qq.com/course/lis/?mt=1001&st=2064&page={i}'
