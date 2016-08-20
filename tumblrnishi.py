import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


def nishipic():
    url='https://www.tumblr.com/search/%E8%A5%BF%E6%98%8E%E6%97%A5%E9%A6%99/recent'

    data={}
    data['q']='西明日香'
    data['sort']='recent'
    data['post_view']='masonry'
    data['blogs_before']=-1
    data['num_blogs_shown']=0
    data['num_posts_shown']=0
    data['before']=0
    data['blog_page']=2
    data['post_page']=1
    data['filter_nsfw']='true'
    data['filter_post_type']='photo'
    data['next_ad_offset']=0
    data['ad_placement_id']=0
    data['more_posts']='true'
        
    data=urllib.parse.urlencode(data).encode('utf-8')    
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
    head['referer']='https://www.tumblr.com/search/%E8%A5%BF%E6%98%8E%E6%97%A5%E9%A6%99/recent'

    req=urllib.request.Request(url,data,head)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf8')
    html=re.sub(r'\\u[0-9a-fA-F]{4}', lambda x:eval('"' + x.group() + '"'), html)
    soup=BeautifulSoup(html, "html.parser")
    tags=soup.select('.photo')

    dic={}

    for tag in tags[:4]:
        if tag.get('src').startswith('https'):
            dic[tag.get('data-pin-url')]=tag.get('src')

    return dic
