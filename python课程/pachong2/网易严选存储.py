import requests
import json
import re
import pymysql
class Wy(object):
    def __init__(self):
        self.url = 'https://you.163.com/xhr/globalinfo//queryTop.json'
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        self.link = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'
        self.goodli = []
        # 数据库连接
        self.conn = pymysql.connect(host='localhost', user='root', password="123456", database='jd', port=3306)
        # 获取游标
        self.cursor = self.conn.cursor()

        pass
    def get_cate(self):
        # 请求网页
        res = requests.get(self.url, headers=self.header)
        res.encoding = 'utf-8'
        info = res.text
        # print(info)
        # json模块
        data = json.loads(info)
        # 字典取值
        cateList = data['data']['cateList']
        for item in cateList:
            cate1_name = item['name']
            subCateGroupList = item['subCateGroupList']
            for sub in subCateGroupList:
                cate2_name = sub['name']
                categoryList = sub['categoryList']
                for cate in categoryList:
                    cate3_name = cate['name']
                    superCategoryId = cate['superCategoryId']
                    id = cate['id']
                    cate3_link = self.link.format(superCategoryId,id)
                    self.get_good(cate1_name,cate2_name,cate3_name,cate3_link)
                    if len(self.goodli) > 0:
                        for i in self.goodli:
                            dat = {k: '"' + str(v) + '"' for k, v in i.items()}
                            sql = f'INSERT INTO huicong(cate1, cate2,cate3,name,price,img,desc) VALUES({dat["cate1"]},{dat["cate2"]},{dat["cate3"]},{dat["name"]},{dat["price"]},{dat["img"]},{dat["desc"]})'
                            self.save(sql)
        self.cursor.close()
        self.conn.close()

                    # print(dic)
        pass
    def get_good(self,cate1,cate2,cate3,cate3_link):
        # 请求网页
        response = requests.get(cate3_link, headers=self.header)
        # 指定编码格式
        response.encoding = 'utf-8'
        # 输出响应文本
        info = response.text
        # 运用正则匹配所需字符串
        res = re.findall('var json_Data=(.*)};', info)
        # print(res[0])
        text = res[0] + '}'
        # json数据类型转化
        dta = json.loads(text)
        # 字典取值
        categoryItemList = dta['categoryItemList']
        for item in categoryItemList:
            itemList = item['itemList']
            for i in itemList:
                good = {}
                name = i['name']
                simpleDesc = i['simpleDesc']
                retailPrice = i['retailPrice']
                scenePicUrl = i['scenePicUrl']+'?type=webp&imageView'
                good['name'] = name
                good['desc'] = simpleDesc
                good['price'] = retailPrice
                good['img'] = scenePicUrl
                good['cate1'] = cate1
                good['cate2'] = cate2
                good['cate3'] = cate3
                self.goodli.append(good)

                # 'https://yanxuan-item.nosdn.127.net/b7d5a39aca6b0bf27991d2f6ef30f071.jpg'
                # 'https://yanxuan-item.nosdn.127.net/b7d5a39aca6b0bf27991d2f6ef30f071.jpg?type=webp&imageView'
            pass
        pass
    def save(self,sql):
        # 1.连接数据库
        # 2.获取游标
        # 执行SQL语句
        # 插入语句
        self.cursor.execute(sql)
        # 提交数据
        self.conn.commit()
        # conn.close()
        pass

    pass
