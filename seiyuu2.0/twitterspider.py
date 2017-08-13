import requests
import json
import urllib
import re
from bs4 import BeautifulSoup

def spider(twitter_name, limit=99):
    dic={}
    link='https://twitter.com/' + twitter_name
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html, "html.parser")

    avatarimage=soup.select('.ProfileAvatar-image')[0].get('src')
    tags=soup.select('li')

    
    for tag in tags:
        message=''
        pics=[avatarimage]
              
        if len(tag.select('.TweetTextSize '))>0:
            if tag.select('p')[0].text!=tag.select('.TweetTextSize ')[0].text:
                message=tag.select('p')[0].text+tag.select('.TweetTextSize ')[0].text
            else:
                message=tag.select('p')[0].text
            if len(tag.select('.QuoteTweet-text'))>0:
                message=message+tag.select('.QuoteTweet-text')[0].text
                for each in tag.select('.QuoteMedia-photoContainer'):
                    pics.append(each.get('data-image-url'))
            if len(tag.select('.AdaptiveMedia-photoContainer'))>0:
                for each in tag.select('.AdaptiveMedia-photoContainer'):
                    pics.append(each.get('data-image-url'))
            # check if there are more than 3 japanese characters or KANJI in the message
            if len(re.findall(r'[\u3041-\u30F6\u4E00-\u9FA0]',message))>3 or len(message)<40:
                dic[message]=pics
        if len(dic)+1>limit:
            return dic            
    return dic

