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
r1 = html.etree.HTML(a)
r22 = r1.xpath('//div[@class="TwoBox02"]/div[@class="TwoBox02_01"]')
for i in r22:
    a1 = i.xpath('.//div[@class="TwoBox02_08"]//a/@title')[0]
    a2 = i.xpath('.//div[@class="TwoBox02_08"]//a/@title')[1]
    p1 = i.xpath('.//div[@class="TwoBox02_03"]/a/img/@src')[0]
    p2 = i.xpath('.//div[@class="TwoBox02_03"]/a/img/@src')[1]
    print(a1, p1, a2, p2)
    s = requests.get(p1, headers=header)
    s1 = requests.get(p2, headers=header)
    if s.status_code == 200:
        with open(f"img/{a1}.jpg", "ab") as f:
            f.write(s.content)
    if s1.status_code == 200:
        with open(f"img/{a2}.jpg", "ab") as f:
            f.write(s1.content)
