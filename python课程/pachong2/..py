import requests
import json
import csv
with open('wb.csv', 'a+', newline="") as f:
    obj = csv.writer(f)
    obj.writerow(['名字','链接','排名'])
    url = 'https://weibo.com/ajax/side/hotSearch'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
    }
    res = requests.get(url, headers=header)
    res.encoding = 'utf-8'
    info = json.loads(res.text)
    realtime = info['data']['realtime']
    for ite in realtime:
        row = []
        note = ite['note']
        a = f'https://s.weibo.com/weibo?q=%23{note}%23&topic_ad='
        rank = int(ite['rank'])+1
        row = [note,a,rank]
        print(note,rank)
        obj.writerow(row)