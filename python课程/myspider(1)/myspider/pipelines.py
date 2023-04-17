# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from myspider.opMysql import Sql # 导入数据库操作

class MyspiderPipeline:
    def process_item(self, item, spider):
        #操作数据库（增删改查）
        try:
            Sql.insert_chinaz(item)
        except Exception as ex:
            print(ex.args)
        return item
