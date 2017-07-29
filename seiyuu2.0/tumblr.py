import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


def gettumblr(name, limit=99):
    
    url='https://www.tumblr.com/search/' + urllib.parse.quote(name) + '/recent'

    html=urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup( html, "html.parser" )
    tags=soup.select('.photo')

    dic={}

    for tag in tags:
        
        if len(dic)+1>limit:
            break
        else:
            if tag.get('data-pin-url'):        
                if tag.get('src').startswith('https'):
                    dic[tag.get('data-pin-url')]=[tag.get('src')]
                else:
                    dic[tag.get('data-pin-url')].append(tag.get('data-src'))

    return dic
