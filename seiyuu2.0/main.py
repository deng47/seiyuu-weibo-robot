#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import time, datetime
from weibo_login import *
from sendweibo import *
from news import *
from bilibili import *
from tumblr import *
from now import *
from twitterspider import *
from event import *
from poollog import *

def updatetwitter(name, tag):
    global count, limit, pool
    pool=readpool(pool, tag)
    try:        
        weibos=spider(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, pausetime, weibos[each])

    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)
        
def updatetumblr(name, tag):
    global count, limit, pool
    pool=readpool(pool, tag)
    try:
        weibos=gettumblr(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, pausetime, weibos[each])
                
    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)        
        
def updatenews(name, tag):
    global count, limit, pool
    pool=readpool(pool, tag)
    try:
        weibos=getnews(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, pausetime, weibos[each])

    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)   

def updatebilibili(name, tag):
    global count, limit, pool
    pool=readpool(pool, tag)
    try:
        weibos=getbili(name, limit)
        for each in weibos:
            if each not in pool:
                count=send(count, pool, tag, each, pausetime, weibos[each])
                
    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)         

def updateevent(name, tag):
    global count, pool
    pool=readpool(pool, tag)
    try:
        weibos=getevent(name)
        if len(weibos)>0:
            for each in weibos:
                if each not in pool:
                    count=send(count, pool, tag, each, pausetime, weibos[each])
        else:
            pass
                
    except:
        log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
        time.sleep(pausetime)    
        

#设立抓取库
log('+++++++++++++++++++++++++++++++++++++++++++++\n+++++'+str(time.asctime( time.localtime(time.time())))+' 程序启动  +++++\n+++++++++++++++++++++++++++++++++++++++++++++\n')
limit=7
pool=[]
count=0
pausetime=5
start_time=datetime.datetime.now()

print(time.asctime(time.localtime(time.time())),' +++++ 循环开始 +++++')

#更新twitter

name='seaside_c'
tag='#シーサイド コミュニケーションズ#twitter:'
updatetwitter(name, tag)    
update(pool, tag, limit)

name='kinmosa_anime'
tag='#ＴＶアニメ「きんいろモザイク」#twitter:'
updatetwitter(name, tag)
update(pool, tag, limit)

name='suzakinishi'
tag='#洲崎西#twitter:'
updatetwitter(name, tag)
update(pool, tag, limit)

name='suzakiaya7_6'
tag='「洲崎綾の7.6」公式twitter:'
updatetwitter(name, tag)
update(pool, tag, limit)

name='suzaki_aya'
tag='#洲崎綾#三十路記念twitter:'
updatetwitter(name, tag)
update(pool, tag, limit)

name='nishi_deliradi'
tag='#西明日香のデリケートゾーン！#twitter:'
updatetwitter(name, tag)
update(pool, tag, limit)

name='nishiasuka_info'
tag='#西明日香#公式ツイッター:'
updatetwitter(name, tag)   
update(pool, tag, limit)
    
name='seaside_ueki'
tag='#植木雄一郎#twitter:'
updatetwitter(name, tag) 
update(pool, tag, limit)
    
name='akekodao'
tag='#明坂聡美#twitter:'
updatetwitter(name, tag)
update(pool, tag, limit)

#洲崎绫now    
try:
    tag='#洲崎綾#さんのなうhttp://now.ameba.jp/clown-happy/'
    pool=readpool(pool, '#洲崎綾#さんのなう')
    weibos=getnow(limit+3)
    for each in weibos:
        if each not in pool:
            count=send(count, pool, tag, each, pausetime, weibos[each])
    update(pool, '#洲崎綾#さんのなう', limit)
        
except:
    log(str(time.asctime( time.localtime(time.time())))+' !!!!!更新%s出错，休眠%s秒跳过!!!!!\n' % (tag, str(pausetime)))
    time.sleep(pausetime)                

    
#更新 tumblr

name='洲崎綾'
tag='#洲崎綾##tumblr#'
updatetumblr(name, tag)
update(pool, tag, limit)

name='西明日香'
tag='#西明日香##tumblr#'
updatetumblr(name, tag)
update(pool, tag, limit)

name='種田梨沙'
tag='#種田梨沙##tumblr#'
updatetumblr(name, tag)
update(pool, tag, limit)

name='佐倉綾音'
tag='#佐倉綾音##tumblr#'
updatetumblr(name, tag)   
update(pool, tag, limit)


#更新news

name='洲崎綾'
tag='#洲崎绫##News#'   
updatenews(name, tag)
update(pool, tag, limit)

name='西明日香'
tag='#西明日香##News#'   
updatenews(name, tag)
update(pool, tag, limit)

name='種田梨沙'
tag='#種田梨沙##News#'   
updatenews(name, tag)
update(pool, tag, limit)

name='佐倉綾音'
tag='#佐倉綾音##News#'   
updatenews(name, tag)
update(pool, tag, limit)


#更新bilibili

name='洲崎西'
tag='#洲崎西##bilibili#'        
updatebilibili(name, tag)
update(pool, tag, limit)

name='洲崎绫'
tag='#洲崎绫##bilibili#'        
updatebilibili(name, tag)
update(pool, tag, limit)

name='西明日香'
tag='#西明日香##bilibili#'        
updatebilibili(name, tag)
update(pool, tag, limit)

name='種田梨沙'
tag='#種田梨沙##bilibili#'        
updatebilibili(name, tag)
update(pool, tag, limit)

name='佐倉綾音'
tag='#佐倉綾音##bilibili#'        
updatebilibili(name, tag)   
update(pool, tag, limit)

#更新event

name='洲崎綾/3902'
tag='#洲崎绫##Event countdown#'    
updateevent(name, tag)
update(pool, tag, limit)

name='西明日香/2470'
tag='#西明日香##Event countdown#'    
updateevent(name, tag)
update(pool, tag, limit)

name='種田梨沙/3528'
tag='#種田梨沙##Event countdown#'    
updateevent(name, tag)
update(pool, tag, limit)

name='佐倉綾音/2650'
tag='#佐倉綾音##Event countdown#'    
updateevent(name, tag)
update(pool, tag, limit)

      
#打印运行状态
end_time=datetime.datetime.now()
log('+++++\n+++++'+str(time.asctime( time.localtime(time.time())))+' 运行时间：'+str(end_time-start_time)+' 发送微博%d条+++++\n+++++\n' % count)

print(time.asctime(time.localtime(time.time())),' 循环执行完毕，发送微博%s条' % (str(count)))		

