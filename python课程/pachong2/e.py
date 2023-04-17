import requests
from lxml import html
url = "https://www.hc360.com/"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
response = requests.get(url, headers=header)
response.encoding('utf-8')
html = html.etree.HTML(response.text)
li = html.xpath('')
print(li)