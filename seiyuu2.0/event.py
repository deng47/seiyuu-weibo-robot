
#eventernote爬虫

import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import re
import datetime

def getevent(name):

    url='https://www.eventernote.com/actors/' + urllib.parse.quote(name)
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html, "html.parser")

    contents=soup.find_all('div','date')
    detail=soup.find_all('div','actor')
    place=soup.find_all('div','place')
    
    event={}

    for index, content in enumerate(contents):
        title=re.findall(r'alt="(.*)" height',str(content))[0]
        pic=re.findall(r'src="(.*)" width',str(content))[0]
        
        location=place[index].get_text().lstrip('\n ')
        
        date=content.get_text()
        eventdate=datetime.datetime.strptime(date[1:11], '%Y-%m-%d')
        today=datetime.datetime.now()
        countdown=(eventdate-today).days+1
        if countdown==1:
            actor=detail[index].get_text()
            message=(str(countdown)+' day left\n'+title+date+location+actor).replace('\n\n','\n')
            message=message.replace('\n\n','\n')
            event[message]=[pic]

        elif countdown==7 or countdown%30==1:
            actor=detail[index].get_text()
            message=(str(countdown)+' days left\n'+title+date+location+actor).replace('\n\n','\n')
            message=message.replace('\n\n','\n')
            event[message]=[pic]
            
    return event






