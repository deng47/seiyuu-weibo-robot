import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

def getbili(name, limit=99):
        
    dic={}
    url='http://search.bilibili.com/ajax_api/video?keyword=' + urllib.parse.quote(name) + '&page=1&order=pubdate&tids_1=13&tids_2=152'
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf8')
    soup=BeautifulSoup(html, "html.parser")
    tags=soup.select('a')

    for tag in tags:
        if len(dic)+1 > limit:
            break
        link = tag.get('href')[4:-2]
        if link.startswith('www.bilibili') and re.search(r'[^\x00-\xff]',tag.text)!=None:
            link=link[:link.find('?from')]
            dic[tag.text[10:-8]+' http://'+link] = []

    return dic





