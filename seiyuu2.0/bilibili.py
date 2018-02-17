import urllib.request
import urllib.parse
import json

def getbili(name, limit=99):
        
    dic={}
    url='http://search.bilibili.com/api/search?search_type=all&keyword=' + urllib.parse.quote(name) + '&from_source=nav_search&order=pubdate&duration=0&tids_1=13&tids_2=152'
    html=urllib.request.urlopen(url).read().decode('utf8')
    j=json.loads(html)
    for each in j['result']['video']:
        if len(dic) < limit:
            if each['typeid'] == '152':
                dic[each['arcurl']+"\nUP主: "+each['author']+"\n"+each['description']] = []

    return dic

