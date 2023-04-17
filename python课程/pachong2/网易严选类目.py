import requests
import json
import re
import csv
f = open("file.csv","w",encoding="utf-8",newline="")
def get_cate1():

    #三级类目链接
    link3 = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'
    #请求url
    url = 'https://you.163.com/xhr/globalinfo//queryTop.json'
    #请求头信息
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    #请求页面信息
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    res = response.text
    # print(res)
    #使用json模块
    info = json.loads(res)
    #字典取值
    cateList = info['data']['cateList']
    for item in cateList:
        cate1 = item['name']
        subCateGroupList = item['subCateGroupList']
        for sub in subCateGroupList:
            cate2 = sub['name']
            categoryList = sub['categoryList']
            for cate in categoryList:
                cate3 = cate['name']
                superCategoryId = cate['superCategoryId']
                id = cate['id']
                #三级类目拼接
                cate3_link = link3.format(superCategoryId, id)
                print(cate1, cate2, cate3, cate3_link)
                'https://you.163.com/item/list?categoryId=1005000&subCategoryId=1008009'

                'https://you.163.com/item/list?categoryId=1008009&subCategoryId=1005000'

def get_cate2():
    '该请求没有二级类目'
    url = 'https://you.163.com/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    #请求网页
    response = requests.get(url,headers =header)
    response.encoding = 'utf-8'
    res = response.text
    # print(res)
    #使用正则匹配数据
    info_li = re.findall('"cateList": (.*)\],',res)
    # print(info_li[0]+']')
    info = info_li[0]+']'
    #json模块
    data = json.loads(info)
    # 字典取值
    for item in data:
        cate1 = item['name']
        subCateList = item['subCateList']
        for sub in subCateList:
            cate3 = sub['name']
            superCategoryId = sub['superCategoryId']
            id = sub['id']
            cate3_link = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'.format(superCategoryId, id)
            print(cate1, cate3, cate3_link)
            with open("info6.CSV", "a", newline='') as f:
                title = ['类目','商品','连接']
                row = [cate1, cate3, cate3_link]
                write = csv.writer(f)
                write.writerow(row)


#调用方法
get_cate2()
