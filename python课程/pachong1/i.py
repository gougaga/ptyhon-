# post  请求
import urllib.request
import json
# 构造对象request对象
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
data = {
    "kw": "bla"
}
# 参数格式转化
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
request = urllib.request.Request(url, headers=header, data=info)
response = urllib.request.urlopen(request)
res = response.read().decode('utf-8')
print(json.loads(res))