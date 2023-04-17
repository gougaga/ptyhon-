import requests
from lxml import html
url = "https://b.faloo.com/y_0_1.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
request = requests.get(url, headers=header)
request.encoding = 'gbk'
a = request.text
# print(a)
res = html.etree.HTML(a)
res1 = res.xpath('//div[@class="TwoBox02"]/div[@class="TwoBox02_01"]')
for i in res1:
    res2 = i.xpath('.//div[@class="TwoBox02_08"]//a/@title')[0]
    res3 = i.xpath('.//div[@class="TwoBox02_08"]//a/@title')[1]
    p1 = i.xpath('.//div[@class="TwoBox02_03"]/a/img/@src')[0]
    p2 = i.xpath('.//div[@class="TwoBox02_03"]/a/img/@src')[1]
    print(res2, p1, res3, p2)
    ss1 = requests.get(p1, headers=header)
    ss2 = requests.get(p2, headers=header)
    if ss1.status_code == 200:
        with open(f"img/{res2}.jpg", "ab") as f:
            f.write(ss1.content)
    if ss2.status_code == 200:
        with open(f"img/{res3}.jpg", "ab") as f:
            f.write(ss2.content)