
#hackdoll站新闻爬虫
#洲崎绫相关

import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import re

def getsuzaki():
    url='https://web.hackadoll.com/search?q=%E6%B4%B2%E5%B4%8E%E7%B6%BE'
    req=urllib.request.Request(url)
    res=urllib.request.urlopen(req)
    webpage=res.read().decode('utf8')
    soup=BeautifulSoup(webpage, "html.parser")

    script=soup.select('script')
    #查找新闻列表部分代码
    raw=script[7].text

    start=raw.find('JSON.parse')+12
    end=raw.find('||')-2

    #找出json部分并把unicode转码
    data=raw[start:end]
    data=re.sub(r'\\u[0-9a-fA-F]{4}', lambda x:eval('"' + x.group() + '"'), data)

    #只抓取前n条新闻
    newslist=json.loads(data)[:4]

    #提取题目、内容、链接、图片
    dic={}
    
    for each in newslist:
        dic[each['title']]=[each['publisher'],each['publisher'],each['pcUrl'],each['images'][0]['url']]
    return dic
