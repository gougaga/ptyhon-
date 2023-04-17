
import scrapy


class TXKTspider(scrapy.Spider):
    name = 'txt'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/course/list?mt=1001']

    def parse(self, response):
        # response是我们的响应
        # 1.转换文档数对象
        # 2.使用xpath解析拿到的数据,之前确定的3个字段
        a = response.xpath('//div[@class="course-list"]/div')
        for b in a:
            name = b.xpath('.//div[@class="kc-course-card-cover"]/img/@src').extract_first()  # 名称
            info = b.xpath('.//div[@class="kc-course-card-content"]/h3/@title').extract_first()  # 简介

            print(name, info)

            yield {
                '名字': info,
                '链接': name

            }
pass


