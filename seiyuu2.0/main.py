import time, datetime
from weibo_login import *
from sendweibo import *
from news import *
from bilibili import *
from tumblr import *
from now import *
from twitterspider import *


#设立抓取库
pool=[]
count=0
pausetime=30
start_time=datetime.datetime.now()

def updatetwitter(name, tag):
    global limit, count      
    try:
        weibos=spider(name, limit)
        for each in weibos:
            if each not in pool:
                send(tag+each,weibos[each])
                count+=1
                pool.append(each)
        print(time.asctime( time.localtime(time.time()) ),'完成更新:',tag)
    except:
        print(time.asctime( time.localtime(time.time()) ),'更新%s出错，休眠%s秒跳过' % (tag, str(pausetime)))
        time.sleep(pausetime)
        
def updatetumblr(name, tag):
    global limit, count  
    try:
        weibos=gettumblr(name, limit)
        for content in weibos:
            if content not in pool:
                message=tag+content
                pics=weibos[content]
                send(message,pics)
                count+=1
                pool.append(content)
        print(time.asctime( time.localtime(time.time()) ),'完成更新:',tag)
    except:
        print(time.asctime( time.localtime(time.time()) ),'更新%s出错，休眠%s秒跳过' % (tag, str(pausetime)))
        time.sleep(pausetime)

def updatenews(name, tag):
    global limit, count    
    try:	
        weibos=getnews(name, limit)
        for title in weibos:
            if title in pool:
                continue
            else:
                message=tag+title+weibos[title][0]+weibos[title][1]
                pics=weibos[title][2]		
                send(message,pics)
                count+=1
                pool.append(title)
        print(time.asctime( time.localtime(time.time()) ),'完成更新:',tag)
    except:
        print(time.asctime( time.localtime(time.time()) ),'更新%s出错，休眠%s秒跳过' % (tag, str(pausetime)))
        time.sleep(pausetime)                                
        
def updatebilibili(name, tag, limit):
    global count    
    try:    
        pic=[]
        videos=getbili(name, limit)
        for link in videos:
            if link not in pool:		
                message=tag+link
                send(message,pic)
                count+=1
                pool.append(link)    
    except:
        print(time.asctime( time.localtime(time.time()) ),'更新%s出错，休眠%s秒跳过' % (tag, str(pausetime)))
        time.sleep(pausetime)

while True:

    #更新twitter
    
    limit=3

    name='seaside_c'
    tag='#シーサイド コミュニケーションズ#twitter:'
    updatetwitter(name, tag)    
    
    name='kinmosa_anime'
    tag='#ＴＶアニメ「きんいろモザイク」#twitter:'
    updatetwitter(name, tag)
    
    name='suzakinishi'
    tag='#洲崎西#twitter:'
    updatetwitter(name, tag)
        
    name='suzakiaya7_6'
    tag='「洲崎綾の7.6」公式twitter:'
    updatetwitter(name, tag)
        
    name='nishi_deliradi'
    tag='#西明日香のデリケートゾーン！#twitter:'
    updatetwitter(name, tag)
    
    name='nishiasuka_info'
    tag='#西明日香公式ツイッター#:'
    updatetwitter(name, tag)   
        
    name='seaside_ueki'
    tag='#植木雄一郎#twitter:'
    updatetwitter(name, tag) 
        
    name='akekodao'
    tag='#明坂聡美#twitter:'
    updatetwitter(name, tag) 

    #洲崎绫now    
    try:

        weibos=getnow(limit*2)
        for content in weibos:
            if content not in pool:                
                message='#洲崎綾#さんのなう '+content+' http://now.ameba.jp/clown-happy/'
                pics=weibos[content]
                send(message,pics)
                count+=1
                pool.append(content)
        print(time.asctime( time.localtime(time.time()) ),'完成更新洲崎綾さんのなう')

    except:
        print(time.asctime( time.localtime(time.time()) ),'更新%s出错，休眠%s秒跳过' % (tag, str(pausetime)))
        time.sleep(pausetime)                

        
    #更新 tumblr
    
    name='洲崎綾'
    tag='#洲崎綾##tumblr# '
    updatetumblr(name, tag)
    
    name='西明日香'
    tag='#西明日香##tumblr# '
    updatetumblr(name, tag)

    name='種田梨沙'
    tag='#種田梨沙##tumblr# '
    updatetumblr(name, tag)

    name='佐倉綾音'
    tag='#佐倉綾音##tumblr# '
    updatetumblr(name, tag)   

    #更新news
    
    name='洲崎綾'
    tag='#洲崎绫##News#'   
    updatenews(name, tag)
    
    name='西明日香'
    tag='#西明日香##News#'   
    updatenews(name, tag)
    
    name='種田梨沙'
    tag='#種田梨沙##News#'   
    updatenews(name, tag)
    
    name='佐倉綾音'
    tag='#佐倉綾音##News#'   
    updatenews(name, tag)

    #更新bilibili
    
    name='洲崎西'
    tag='#洲崎西##bilibili#'        
    updatebilibili(name, tag, limit)
    
    name='洲崎绫'
    tag='#洲崎绫##bilibili#'        
    updatebilibili(name, tag, limit*2)

    name='西明日香'
    tag='#西明日香##bilibili#'        
    updatebilibili(name, tag, limit*2)

    name='種田梨沙'
    tag='#種田梨沙##bilibili#'        
    updatebilibili(name, tag, limit)

    name='佐倉綾音'
    tag='#佐倉綾音##bilibili#'        
    updatebilibili(name, tag, limit)   
    
        
    #更新列表库           
    if len(pool)>limit*1000:
        pool=pool[-limit*1000:]
                    
    #打印运行状态
    end_time=datetime.datetime.now()
    print(time.asctime( time.localtime(time.time()) ),'累计发送微博%d条' % count)
    print('累计运行时间：',(end_time-start_time))
    print('启动休眠%s分钟' % str(pausetime//3))
    time.sleep(pausetime*20)


		
		

