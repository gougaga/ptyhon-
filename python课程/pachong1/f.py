import urllib.request

link = 'http://python.org'
#html = response.read().decode('utf-8')
#print(html)
#print(type(response))
#print(response.geturl())  # 请求网址
#print(response.getcode())  # 状态码
#print(response.info())  # 网页元信息


header = {
}
request = urllib.request.Request(link, headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
#print(html)
print(type(response))
print(response.geturl())  # 请求网址
print(response.getcode())  # 状态码
print(response.info())  # 网页元信息

lin = 'https://www.jd.com'
header = {
    'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
}
request = urllib.request.Request(lin, headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(type(request))
print(response.geturl())  # 请求网址
print(response.getcode())  # 状态码
print(response.info())  # 网页元信息

