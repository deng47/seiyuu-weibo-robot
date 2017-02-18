

def log(record):
    file = open('log.txt','a', encoding='utf-8')
    file.write(str(record))
    file.close()

def save(pool):
    file = open('checkpoint.txt','w', encoding='utf-8')
    file.write(str(pool))
    file.close()