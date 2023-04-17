import requests
import json
#带参数的get请求
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
url = {
    "https://httpbin.org/get"
}
pas = {
    "name":"阿萨",
    "clss":"2",
    "age":"100"
}
res = requests.get(url, params=pas)
print(json.loads(res.text))