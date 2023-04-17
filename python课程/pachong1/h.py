import urllib.request
import urllib.parse

link = 'https://www.baidu.com/s?'
# 构造request对象
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
dic = {
    'wd': '河南艺术职业学院'
}
link_url = urllib.parse.urlencode(dic)
finurl = link + link_url
request = urllib.request.Request(finurl, headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)