from weibo import Client
import urllib.request
import urllib.parse
from suzaki import *
from taneda import *
from nishi import *
from sakura import *
import time
import datetime
from bilisuzaki import *
from bilinishi import *
from bilitaneda import *
from bilisakura import *
from tumblrsuzaki import *
from tumblrnishi import *
from tumblrtaneda import *
from tumblrsakura import *
from suzakinow import *


#取得微博应用权限
c = Client()
print(c.authorize_url)
c.set_code(input("Input code:"))
token = c.token

start_time=datetime.datetime.now()
print(time.asctime( time.localtime(time.time()) ),'开始运行')

#设立新闻抓取新闻列表和b站视频列表及汤不热图片列表
newspool=[]
count=0
avpool=[]
avcount=0
tumblrpool=[]
tumblrcount=0
nowpool=[]
nowcount=0

warning='Warning: 图片来自汤不热，标签内容比较混乱，可能会对不上'

while True:

    #容错
    try:
        
        #获取洲崎绫now、各人的汤不热、b站最新视频及新闻列表，加上关键字后发微博
               
        #洲崎绫now
        nowdic=getnow()
        
        for content in nowdic:
            if content not in nowpool and nowdic[content]!=None:
                try:
                    req=urllib.request.Request(nowdic[content])
                    res=urllib.request.urlopen(req)
                    print('now图片微博')
                    c.post('statuses/upload', status='#洲崎綾#さんのなう  '+content+' http://now.ameba.jp/clown-happy/', pic=res)
                    nowcount+=1
                    print(datetime.datetime.now(),'now发送成功: ',content)
                    nowpool.append(content)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue   
            elif content not in nowpool:
                nowpool.append(content)
                c.post('statuses/update', status='#洲崎綾#さんのなう  '+content+' http://now.ameba.jp/clown-happy/')
                nowcount+=1
                print(datetime.datetime.now(),'now发送成功: ',content)
                time.sleep(60)                
               
        #洲崎绫
        tumblr=suzakipic()
        
        for content in tumblr:
            if content not in tumblrpool:
                try:
                    req=urllib.request.Request(tumblr[content])
                    res=urllib.request.urlopen(req)
                    print('尝试发汤不热图片微博')
                    c.post('statuses/upload', status=content, pic=res)
                    tumblrcount+=1
                    print(datetime.datetime.now(),'发送成功: ',content)
                    tumblrpool.append(content)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue            
        
        suzakivideos=avsuzaki()[:4]
        
        for link in suzakivideos:
            if link not in avpool:
                avpool.append(link)
                c.post('statuses/update', status='#洲崎绫# '+link)
                avcount+=1
                print(datetime.datetime.now(),'发送成功: ',link)
                time.sleep(60)
                
        suzakidic=getsuzaki()
        
        for title in suzakidic:
            if title in newspool:
                continue
            else:
                contents='#洲崎绫# '+title+suzakidic[title][0]+suzakidic[title][2]
                piclink=suzakidic[title][3]
                try:
                    req=urllib.request.Request(piclink)
                    res=urllib.request.urlopen(req)
                    print('尝试发微博')
                    c.post('statuses/upload', status=contents, pic=res)
                    count+=1
                    print(datetime.datetime.now(),'发送成功: ',title)
                    newspool.append(title)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue

        #西明日香    
        tumblr=nishipic()
        
        for content in tumblr:
            if content not in tumblrpool:
                try:
                    req=urllib.request.Request(tumblr[content])
                    res=urllib.request.urlopen(req)
                    print('尝试发汤不热图片微博')
                    c.post('statuses/upload', status=content, pic=res)
                    tumblrcount+=1
                    print(datetime.datetime.now(),'发送成功: ',content)
                    tumblrpool.append(content)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue            

        nishivideos=avnishi()[:4]
        
        for link in nishivideos:
            if link not in avpool:
                avpool.append(link)
                c.post('statuses/update', status='#西明日香# '+link)
                avcount+=1
                print(datetime.datetime.now(),'发送成功: ',link)
                time.sleep(60)            
        
        nishidic=getnishi()
        
        for title in nishidic:
            if title in newspool:
                continue
            else:
                contents='#西明日香# '+title+nishidic[title][0]+nishidic[title][2]
                piclink=nishidic[title][3]
                try:
                    req=urllib.request.Request(piclink)
                    res=urllib.request.urlopen(req)
                    print('尝试发微博')
                    c.post('statuses/upload', status=contents, pic=res)
                    count+=1
                    print(datetime.datetime.now(),'发送成功: ',title)
                    newspool.append(title)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue
                
        #種田梨沙
        tumblr=tanedapic()
        
        for content in tumblr:
            if content not in tumblrpool:
                try:
                    req=urllib.request.Request(tumblr[content])
                    res=urllib.request.urlopen(req)
                    print('尝试发汤不热图片微博')
                    c.post('statuses/upload', status=content, pic=res)
                    tumblrcount+=1
                    print(datetime.datetime.now(),'发送成功: ',content)
                    tumblrpool.append(content)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue                 
        
        tanedavideos=avtaneda()[:4]
        
        for link in tanedavideos:
            if link not in avpool:
                avpool.append(link)
                c.post('statuses/update', status='#種田梨沙# '+link)
                avcount+=1
                print(datetime.datetime.now(),'发送成功: ',link)
                time.sleep(60)            
                
        tanedadic=gettaneda()
        
        for title in tanedadic:
            if title in newspool:
                continue
            else: 
                contents='#種田梨沙# '+title+tanedadic[title][0]+tanedadic[title][2]
                piclink=tanedadic[title][3]
                try:
                    req=urllib.request.Request(piclink)
                    res=urllib.request.urlopen(req)
                    print('尝试发微博')
                    c.post('statuses/upload', status=contents, pic=res)
                    count+=1
                    print(datetime.datetime.now(),'发送成功: ',title)
                    newspool.append(title)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue            
        
        #佐倉綾音
        tumblr=sakurapic()
        
        for content in tumblr:
            if content not in tumblrpool:
                try:
                    req=urllib.request.Request(tumblr[content])
                    res=urllib.request.urlopen(req)
                    print('尝试发汤不热图片微博')
                    c.post('statuses/upload', status=content, pic=res)
                    tumblrcount+=1
                    print(datetime.datetime.now(),'发送成功: ',content)
                    tumblrpool.append(content)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue               
        
        sakuravideos=avsakura()[:4]
        
        for link in sakuravideos:
            if link not in avpool:
                avpool.append(link)
                c.post('statuses/update', status='#佐倉綾音# '+link)
                avcount+=1
                print(datetime.datetime.now(),'发送成功: ',link)
                time.sleep(60)     
        
        sakuradic=getsakura()

        for title in sakuradic:
            if title in newspool:
                continue
            else:
                contents='#佐倉綾音# '+title+sakuradic[title][0]+sakuradic[title][2]
                piclink=sakuradic[title][3]
                try:
                    req=urllib.request.Request(piclink)
                    res=urllib.request.urlopen(req)
                    print('尝试发微博')
                    c.post('statuses/upload', status=contents, pic=res)
                    count+=1
                    print(datetime.datetime.now(),'发送成功: ',title)
                    newspool.append(title)
                    time.sleep(301)
                except:
                    print(time.asctime( time.localtime(time.time()) ),'达到upload上限，启动10分钟休眠后重试')
                    time.sleep(600)
                    continue    

        #更新列表库           
        if len(avpool)>20:
            avpool=avpool[-20:]            
                       
        if len(newspool)>20:
            newspool=newspool[-20:]

        if len(tumblrpool)>20:
            tumblrpool=tumblrpool[-20:] 
                
        if len(nowpool)>5:
            nowpool=nowpool[-5:] 

        #打印运行状态
        end_time=datetime.datetime.now()
        print(time.asctime( time.localtime(time.time()) ),'运行中')
        print('累计发送新闻链接微博%d条、B站链接微博%d条、汤不热图片%d张、now状态%d条' % (count,avcount,tumblrcount,nowcount))
        print('累计运行时间：',(end_time-start_time))
        
        weibocount=count+avcount+tumblrcount+nowcount
        runtime=end_time-start_time
        
        c.post('statuses/update', status='#运行状态# 累计运行时间：'+runtime+'  累计发送微博：'+weibocount)
        time.sleep(3600)

    except:
        print(time.asctime( time.localtime(time.time()) ),'出错，15分钟后重试')
        time.sleep(900)
        continue

    
    
