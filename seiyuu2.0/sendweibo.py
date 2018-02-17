import time
import urllib.request
from weibo_login import *
import re
from poollog import *
import random

#登录微博
(session, uid) = wblogin()

Referer = "https://www.weibo.com/u/%s/home?wvr=5" % uid
session.headers["Referer"] = Referer
uploadurl = "https://picupload.weibo.com/interface/pic_upload.php?app=miniblog&s=json&mime=image/jpeg&data=1&wm="


def send(count, pool, tag, each, pausetime,piclinks=[]):
    message=tag+each
    pids=''

    if len(piclinks)>0:
        for piclink in piclinks:
            f = session.get( piclink, timeout=30 )
            img = f.content
            resp = session.post( uploadurl, data=img )
            upload_json = re.search( '{.*}}', resp.text ).group(0)
            result = json.loads( upload_json )
            code = result["code"]
            if code == "A00006":
                pid=(result["data"]["pics"]["pic_1"]["pid"])
                pids += " " + pid
            else:
                log(str(time.asctime( time.localtime(time.time())))+' 图片在线上传失败,尝试暂存本地再上传 '+piclink+'\n')
                try:
                    res=urllib.request.Request(piclink)
                    response=urllib.request.urlopen(res)
                    img=response.read()
                    log(str(time.asctime( time.localtime(time.time())))+' 读取在线图片\n')
                    extension=re.findall(r'\.[^.\\/:*?"<>|\r\n]+$',piclink)[0]
                    localpic=open('temp'+extension,'wb')
                    localpic.write(img)
                    localpic.close()
                    log(str(time.asctime( time.localtime(time.time())))+' 成功保存本地图片 '+'temp'+extension+'\n')
                    localpic=open('temp'+extension,'rb')
                    resp = session.post( uploadurl, data=localpic )
                    upload_json = re.search( '{.*}}', resp.text ).group(0)
                    result = json.loads( upload_json )
                    code = result["code"]
                    if code == "A00006":
                        pid=(result["data"]["pics"]["pic_1"]["pid"])
                        pids += " " + pid
                        log(str(time.asctime( time.localtime(time.time())))+' 本地图片上传成功\n')
                except:
                    log(str(time.asctime( time.localtime(time.time())))+message[:10]+'...内容的 本地图片上传失败 '+'temp'+extension+'\n')
                
                localpic.close()                 
            time.sleep(pausetime)

        pids=pids.strip()

    #写入微博文字内容与上传图片pid
    #字数限制
    #if len(message)-len(re.findall(r'[0-9A-z]',message))/2>140:
    #    message=message[:138]+'...'
    data = {
            "location": "v6_content_home",
            "appkey": "",
            "style_type": "1",
            "pic_id": pids,
            "text": message,
            "pdetail": "",
            "rank": "0",
            "rankid": "",
            "module": "stissue",
            "pub_type": "dialog",
            "_t": "0",
            }

    #发出微博
    resp = session.post("https://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%d" % int( time.time() * 1000),data=data)
    weibo_json = re.search( '{.*}}', resp.text ).group(0)
    result = json.loads( weibo_json )
    
    if result["code"]=='100000':
        count+=1
        pool.append(each)
        log(str(time.asctime( time.localtime(time.time())))+' 成功发送微博： %s \n' % message)
    else:
        log("!!!!!code: "+result["code"]+' '+str(time.asctime( time.localtime(time.time())))+' 发送失败： %s !!!!!\n' % message)
    
    if random.randint(0,3) == 0:
        pool.append(each)
        
    time.sleep(pausetime)
    
    return count


