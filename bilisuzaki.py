import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

def avsuzaki():
    url='http://search.bilibili.com/ajax_api/video?keyword=%E6%B4%B2%E5%B4%8E%E7%BB%AB&order=pubdate&page=1&_=1470855576747'
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf8')
    soup=BeautifulSoup(html, "html.parser")
    tags=soup.select('a')

    videolist=[]

    for tag in tags:
        raw=tag.get('href',None)
        if raw!=None and len(raw)>37:
            raw=re.findall(r'http.+av.+/',raw)
            if len(raw)>0 and raw[0] not in videolist:
                videolist.append(raw[0])

    return videolist








