def readpool(pool, tag):
    pool=[]
    try:
        file = open('/home/pi/test/seiyuu2.0/record/'+tag[0:-1]+'.txt','r', encoding='utf-8')
        pool = eval(file.read())
        file.close()
        print('读取'+tag+'更新记录')
    except:
        pass
    return pool   

def log(record):
    try:
        file = open('/home/pi/test/seiyuu2.0/record/'+'log.txt','a', encoding='utf-8')
        file.write(str(record))
        file.close()
    except:
        pass
        
def update(pool, tag, limit):
    if len(pool)>limit*3:
        pool=pool[-limit*3:]  
    file = open('/home/pi/test/seiyuu2.0/record/'+tag[0:-1]+'.txt','w', encoding='utf-8')
    file.write(str(pool))