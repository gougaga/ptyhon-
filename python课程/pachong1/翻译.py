import urllib.request
import urllib.parse
import json
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36","X-Requested-With": "XMLHttpRequest","Cookie": "BIDUPSID=391DEB7EF2C0B39448DA55E40C777986; PSTM=1652337861; BAIDUID=391DEB7EF2C0B39491C13F4F9EB05FF6:FG=1; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=8k052h0k8184a1ala58l7rtg1hj4ptj19; ZFY=aukPR:ATN9FlU5cOKrYECmSU2gCgjgK9Y6MSteVv9i6o:C; BAIDUID_BFESS=391DEB7EF2C0B39491C13F4F9EB05FF6:FG=1; BDRCVFR[FIXrT5n2Tgt]=mk3SLVN4HKm; H_PS_PSSID=26350; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664247204,1664247745,1664250344,1664325623; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664325623; ab_sr=1.0.1_ZWY3OTgxYjc3NTlhYTQ4YWZiMGEyZmJhOWZjOTVlNTJlMjAxNGU4MWRhMjQzMTE0NWVkNThhNGFiZDNiNTNmYzYwN2JmZjA5ZjY1N2UzYWQ0ODhlMzg0YTJlNjA0NGI3N2Y4ZDRlMDliYmM4ZmQ5MWNmODJmOTNkMGNlNmJmZjhkYzAzMGZkZTdiNDk2YWU2NDQ2ODQ2ODBhMDIyYWUzYw=="

}

data = {
    "from": "en",
    "to": "zh",
    "query": "red",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "207046.510967",
    "token": "09ae27da4a6fc96b546e3db42faa7573",
    "domain": "common",
}
# 编码
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
#构造request对象
request = urllib.request.Request(url, headers=header, data=info)
#添加请求头
request.add_header('')
request.add_header()
#urlopen()
response = urllib.request.urlopen(request)
res = response.read().decode('utf-8')
print(json.load(res))