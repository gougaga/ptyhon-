import scrapy


class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['chinaz.com']
    # start_urls = ['http://chinaz.com/']
    start_urls = ['https://top.chinaz.com/hangye/']

    def parse(self, response):
        a = response.xpath('//ul[@class="listCentent"]/li')
        for b in a:
            # dict1 = {}
            data = {}
            name = b.xpath('.//div[@class="CentTxt"]/h3/a/text()').extract_first()
            info = b.xpath('.//p[@class="RtCInfo"]/text()').extract_first()
            rank = b.xpath('.//strong[@class="col-red02"]/text()').extract_first()
            # dict1["名字"] = name[0]
            # dict1["信息"] = info[0]
            # dict1["排名"] = rank[0]
            print(name, info, rank)
            # print(name[0], info[0], rank[0])

            # 方法一: yield返回信息
            yield{
                'name': name,
                'info': info,
                'rank': rank
            }
            # 方法2
            # data['名字'] = name
            # data['简介'] = info
            # data['排名'] = rank
            # yield data

        pass
