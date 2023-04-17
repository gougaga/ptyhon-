import requests
hea = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
link = "https://httpbin.org/get"
# 发送get
response = requests.get(link, header=hea)
#指定编码
response.encoding = 'utf-8'
print(requests.text)

# 编码格式
#请求头放在那里