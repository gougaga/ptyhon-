import requests
from lxml import html

url = 'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8c00b2242d534b85aadd9809fca60d47'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
html = html.etree.HTML(response.text)



cates = html.xpath('//div[@class="fs_col1"]/div') # 所有的类目 12个 包含一级类目 二级类目 三级类目
for cate in cates:
    print(cate)
    cate1 = cate.xpath('//ul[@class="JS_navCtn cate_menu"]') #一级类目
    cate_li = cate.xpath('//div[@class="JS_popCtn cate_pop"]')  # 包含所有三级类目的二级类目列表
    for i in cate_li:
        dict = {}
        cate2 = i.xpath('//div[class = "mod_container"]/text()') # 二级类目
        cate3 = i.xpath('//div[@class="JS_popCtn cate_pop/text()')# 三级类目
        dict['cate1'] = cate1  # 一级类目
        dict['cate2'] = cate2
        dict['cate3'] = cate3
        print(dict)
        print('###########################')