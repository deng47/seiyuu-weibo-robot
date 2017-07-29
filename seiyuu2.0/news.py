
#hackdoll站新闻爬虫

import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import re

def getnews(name, limit=99):

    url='https://web.hackadoll.com/search?q=' + urllib.parse.quote(name)
    req=urllib.request.Request(url)
    res=urllib.request.urlopen(req)
    webpage=res.read().decode('utf8')
    soup=BeautifulSoup(webpage, "html.parser")

    script=soup.select('script')
    #查找新闻列表部分代码
    raw=script[3].text

    start=raw.find('JSON.parse')+12
    end=raw.find('||')-2

    #找出json部分并把unicode转码
    data=raw[start:end]
    data=re.sub(r'\\u[0-9a-fA-F]{4}', lambda x:eval('"' + x.group() + '"'), data)

    #只抓取前n条新闻
    newslist=json.loads(data)

    #提取题目、内容、链接、图片
    dic={}

    for each in newslist[:limit+1]:
            pics=[]
            for image in each['images']:
                    pics.append(image['url'])
            dic[each['title']+' '+each['publisher']+' '+each['pcUrl']]=pics
    return dic
