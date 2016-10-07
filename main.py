#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import time, datetime
from weibo_login import *
from sendweibo import *
from news import *
from bilibili import *
from tumblr import *
from twitterspider import *
from poollog import *

def updatetwitter(name, tag):
    global count, limit, pool
    try:        
        weibos=spider(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, weibos[each])

    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)
        
def updatetumblr(name, tag):
    global count, limit, pool
    try:
        weibos=gettumblr(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, weibos[each])
                
    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)        
        
def updatenews(name, tag):
    global count, limit, pool
    try:
        weibos=getnews(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, weibos[each])

    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)   

def updatebilibili(name, tag):
    global count, limit, pool  
    try:
        weibos=getbili(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, weibos[each])
                
    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)         



#设立抓取库
log('+++++++++++++++++++++++++++++++++++++++++++++\n+++++'+str(time.asctime( time.localtime(time.time())))+' 程序启动  +++++\n+++++++++++++++++++++++++++++++++++++++++++++\n')
limit=7
pool=[]
count=0
pausetime=10
start_time=datetime.datetime.now()

try:
    file = open('checkpoint.txt','r', encoding='utf-8')
    pool = eval(file.read())
    file.close()
    print('读取更新记录')
except:
    pass


print(time.asctime(time.localtime(time.time())),' +++++ 循环开始 +++++')

#更新twitter

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
tag='#西明日香#公式ツイッター:'
updatetwitter(name, tag)   
    
name='seaside_ueki'
tag='#植木雄一郎#twitter:'
updatetwitter(name, tag) 
    
name='akekodao'
tag='#明坂聡美#twitter:'
updatetwitter(name, tag)

#洲崎绫now    
try:

    weibos=getnow(limit+3)
    for each in weibos:
        if each not in pool:
            tag='#洲崎綾#さんのなうhttp://now.ameba.jp/clown-happy/'
            
            count=send(count, pool, tag, each, weibos[each])
            
except:
    log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
    time.sleep(pausetime)                

    
#更新 tumblr

name='洲崎綾'
tag='#洲崎綾##tumblr#'
updatetumblr(name, tag)

name='西明日香'
tag='#西明日香##tumblr#'
updatetumblr(name, tag)

name='種田梨沙'
tag='#種田梨沙##tumblr#'
updatetumblr(name, tag)

name='佐倉綾音'
tag='#佐倉綾音##tumblr#'
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
updatebilibili(name, tag)

name='洲崎绫'
tag='#洲崎绫##bilibili#'        
updatebilibili(name, tag)

name='西明日香'
tag='#西明日香##bilibili#'        
updatebilibili(name, tag)

name='種田梨沙'
tag='#種田梨沙##bilibili#'        
updatebilibili(name, tag)

name='佐倉綾音'
tag='#佐倉綾音##bilibili#'        
updatebilibili(name, tag)   

    
#更新列表库           
if len(pool)>limit*1000:
    pool=pool[-limit*1000:]
                
#打印运行状态
end_time=datetime.datetime.now()
log('+++++\n+++++'+str(time.asctime( time.localtime(time.time())))+' 运行时间：'+str(end_time-start_time)+' 发送微博%d条+++++\n+++++\n' % count)

save(pool)
print(time.asctime(time.localtime(time.time())),' 循环执行完毕，发送微博%s条' % (str(count)))		

