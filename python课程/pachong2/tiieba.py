import requests

url = 'https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=400'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

#response = requests.get(url, heders=header)
#response.encoding = 'utd-8'
#print(response.text)

url = "https://tieba,daidu.com/f"
pa = {
    "kw": "python",
    "pn": 400
}
#response = requests.get(url, params=pa, headers=header)
#response.encoding = 'uft-8'
#print(response.text)
#print(response.status_code)
#print(response.url)
#print(response.content)

# post 请求
url = 'http://httpbin.org/post'
#需要传递的参数
da = {
    'name': 'python',
    'age': 5
}
res = requests.post(url, data=da, headers=header)
res.encoding = 'utf-8'
print(res.text)

#
urll = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
da = {
    'name': 'read'
}
resa = requests.post(urll, data=da, headers=header)
res.encoding = 'utf-8'
print(res.text)