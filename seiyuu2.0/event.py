
#eventernote爬虫

import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import re
import datetime
from poollog import *

def getevent(name):

    url='https://www.eventernote.com/actors/' + urllib.parse.quote(name)
    req=urllib.request.Request(url)
    res=urllib.request.urlopen(req)
    webpage=res.read().decode('utf8')
    soup=BeautifulSoup(webpage, "html.parser")

    content=soup.find_all('div','date')
    detail=soup.find_all('div','actor')
    
    #place=soup.find_all('div','place')
    
    event={}

    for index in range(len(content)):
        title=re.findall(r'alt="(.*)" height',str(content[index]))[0]
        pic=re.findall(r'src="(.*)" width',str(content[index]))[0]
        
        #location=place[index].get_text().lstrip('\n ')
        
        date=content[index].get_text()
        eventdate=datetime.datetime.strptime(date[1:11], '%Y-%m-%d')
        today=datetime.datetime.now()
        countdown=(eventdate-today).days+1
            
        if countdown==1:
            actor=detail[index].get_text()
            message=(str(countdown)+' day left\n'+title+date+actor).replace('\n\n','\n')
            message=message.replace('\n\n','\n')
            event[message]=[pic]

        elif countdown==7 or countdown%30==1:
            actor=detail[index].get_text()
            message=(str(countdown)+' days left\n'+title+date+actor).replace('\n\n','\n')
            message=message.replace('\n\n','\n')
            event[message]=[pic]
            
    return event









