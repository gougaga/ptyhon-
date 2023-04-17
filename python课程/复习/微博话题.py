'''
排名：
//div/span[@class="HotTopic_ranknum_MdimB"]
'''
'''
话题名字：
//div/div[@class="HotTopic_tit_eS4fv"]
'''
import requests
import json
import csv

with open('fgb.csv', 'a+', newline='') as f:
    # 获取csv写入对象
    obj = csv.writer(f)
    # csv文件写入必须以列表形式写入
    obj.writerow(['排名', '名字', '链接', '简介', '阅读量', '讨论量', '类别'])  # 写入第一行，列名
    url = 'https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10'
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header)
    response.encoding = "utf-8"
    info = json.loads(response.text)
    data = info['data']
    statuses = data['statuses']
    for i in statuses:
        row = []
        rank = i['rank']
        topic = i['topic']
        t = f"https://s.weibo.com/weibo?q=%23{topic}%23"
        summary = i['summary']
        read = i['read']
        mention = i['mention']
        claim = i['claim']
        row = [rank, topic, t, summary, read, mention, claim]
        obj.writerow(row)