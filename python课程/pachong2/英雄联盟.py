import requests
import json
import csv
import pandas as pd
# 请求图片地址
img_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'
# 请求地址
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=10'
# 请求头信息
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# 使用requests请求
response = requests.get(url, headers=header)
res = response.text
# 使用json转换字典类型
ress = json.loads(res)
# 字典取值
hero = ress['hero']
#循环从列表中取出所有的英雄
for he in hero:
    heroID = he['heroId']
    name = he['name']
    alias = he['alias']
    print(heroID, name, alias)
    # 把信息写入csv文件
    with open("info2.CSV", "a", newline='') as f:
        row = [id, name, alias]
        write = csv.writer(f)
        write.writerow(row)
        # 拼接图片地址
        img = img_link+heroID+'000.jpg'
        # 把图片写入本地
# 获取每个英雄的第一个皮肤
        #res = requests.get(img)   # 请求图片地址
        #if res.status_code == 200:
            # 写入图片（视频） 二进制
            #with open(f'img/{name}.jpg', 'wb')as f:
                #f.write(res.content)
            # res.content

        # 获取每个英雄多个皮肤并保存
        'https://game.gtimg.cn/images/lol/act/img/skin/big2000.jpg'
        'https://game.gtimg.cn/images/lol/act/img/skin/big2001.jpg'
        'https://game.gtimg.cn/images/lol/act/img/skin/big2002.jpg'
        for k in range(10):
            #img = img_link+heroID+'%03d' % k + '.jpg' # '%03d' % k   [000-009]
            # 拼接一个英雄多张皮肤
            if k <= 9:
                img = img_link+heroID+'00'+str(k)+'.jpg'
            else:
                img = img_link + heroID + '0' + str(k) + '.jpg'
            res = requests.get(img, headers=header) # 请求图片地址
            if res.status_code == 200: # 判断是否请求成功
                with open(f'img/{alias}'+str(k)+'.jpg','ab')as f:
                    f.write(res.content) # 以二进制形式写入图片信息

            pass
