import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

def getnow(limit=99):
    url='http://now.ameba.jp/clown-happy/'
    response=urllib.request.urlopen(url)
    html=response.read().decode('utf8')
    soup=BeautifulSoup(html, "html.parser")

    contents=[]
    images=[]
    dic={}

    tags=soup.select(".text")
    for tag in tags:
        if tag.text not in contents:
            contents.append(tag.text)
    tags=soup.select(".content")
    for tag in tags:
        if re.findall(r'data-original-image="(.+)" src',str(tag))==[]:
            images.append(None)
        else:
            images.append(re.findall(r'data-original-image="(.+)" src',str(tag))[0])
            
    for index in range(limit):
        if images[index] !=None:
            dic[contents[index]]=[images[index]]
        else:
            dic[contents[index]]=[]
    return dic
    
