def readpool(pool, tag):
    pool=[]
    logfolder='/project/seiyuubot/log/'
    try:
        file = open(logfolder+tag[0:-1]+'.txt','r', encoding='utf-8')
        pool = eval(file.read())
        file.close()
        print('读取'+tag+'更新记录')
    except:
        pass
    return pool   

def log(record):
    logfolder='/project/seiyuubot/log/'
    try:
        file = open(logfolder+'log.txt','a', encoding='utf-8')
        file.write(str(record))
        file.close()
    except:
        pass
        
def update(pool, tag, limit):
    logfolder='/project/seiyuubot/log/'
    if len(pool)>30:
        pool=pool[-30:]  
    file = open(logfolder+tag[0:-1]+'.txt','w', encoding='utf-8')
    file.write(str(pool))