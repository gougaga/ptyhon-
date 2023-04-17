import requests
import json
import csv
import pandas as pd
import pymysql
from lxml import html
def get_hero():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    response.encoding = 'gbk'
    page = html.etree.HTML(response.text)
    hero_li = page.xpath('//ul[@class="herolist clearfix"]/li')
    num = 0
    for hero in hero_li:
        name = hero.xpath('.//img/@alt')[0]
        img = hero.xpath('.//img/@src')[0]
        print(name,'https:'+img)
        num+=1
        print(num)

def ger_hero2():
    simg = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}.jpg'
    bsimg = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}-bigskin-2.jpg'
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    conn = pymysql.connect(host='localhost', user='root', password="123456", database='jd', port=3306)
    cursor = conn.cursor()
    response = requests.get(url, headers=header)
    #print(response.text)
    info = json.loads(response.text)
    dict1 = {}
    for item in info:
        ename = str(item['ename'])
        cname = item['cname']
        dict1["ename"] = ename
        dict1["cname"] = cname
        # s_pic = simg.format(ename, ename)
        # skin= bsimg.format(ename, ename)
        # print(ename, cname, s_pic, skin)
        date = {k: "'" + str(v) + "'" for k, v in dict1.items()}
        print(date["ename"])
        sql = f'INSERT INTO yxa(namel, img) VALUES({date["ename"]}, {date["cname"]};'
        cursor.execute(sql)
        # 提交数据
        conn.commit()
    # conn.close()
ger_hero2()