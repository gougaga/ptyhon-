import urllib.request
import urllib.parse
link = "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9c355f87245541089408b9fd96d4dce3"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

request = urllib.request.Request(link, headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)