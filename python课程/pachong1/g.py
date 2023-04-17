import urllib.parse
import urllib.request
info = {
    "名字": "阿斯顿",
    "班级": "阿斯顿"
}

res = urllib.parse.urlencode(info) #编码
da = urllib.parse.unquote(res)  #解码
print(res)
print(da)