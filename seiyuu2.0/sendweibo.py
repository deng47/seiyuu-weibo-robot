import time
import urllib.request
from weibo_login import *
import re

#登录微博
(session, uid) = wblogin()

Referer = "http://www.weibo.com/u/%s/home?wvr=5" % uid
session.headers["Referer"] = Referer
uploadurl = "http://picupload.service.weibo.com/interface/pic_upload.php?rotate=0&app=miniblog&s=json&mime=image/jpeg&data=1&wm="

def send(message, piclinks=[]):

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
                print(time.asctime( time.localtime(time.time()) ),'图片在线上传失败,暂存本地再上传',piclink)
                try:
                    res=urllib.request.Request(piclink)
                    response=urllib.request.urlopen(res)
                    img=response.read()
                    extension=re.findall(r'\.[^.\\/:*?"<>|\r\n]+$',piclink)
                    localpic=open('temp'+extension[0],'wb')
                    localpic.write(img)
                    localpic.close()
                    localpic=open('temp'+extension[0],'rb')
                    resp = session.post( uploadurl, data=localpic )
                    upload_json = re.search( '{.*}}', resp.text ).group(0)
                    result = json.loads( upload_json )
                    code = result["code"]
                    if code == "A00006":
                        pid=(result["data"]["pics"]["pic_1"]["pid"])
                        pids += " " + pid
                        print(time.asctime( time.localtime(time.time()) ),'本地图片上传成功')
                except:
                    print(time.asctime( time.localtime(time.time()) ),'本地图片上传失败','temp'+extension)
                
                localpic.close()                 
            time.sleep(5)

        pids=pids.strip()

    #写入微博文字内容与上传图片pid
    
    if len(message)-len(re.findall(r'[0-9A-z]',message))/2>140:
        message=message[:138]+'...'
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
    session.post("http://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%d" % int( time.time() * 1000),data=data)
    print(time.asctime( time.localtime(time.time()) ),'成功发送微博： %s' % message)
    time.sleep(10)


