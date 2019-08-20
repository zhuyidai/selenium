import time

class Loginfo(object):
    def __init__(self,path = '', mode='w'):
        fname=path+time.strftime('%Y-%m-%d',time.gmtime())
        self.log=open(path+fname+'.txt',mode)

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()

if __name__ == '__main__':
    log=Loginfo()
    log.log.write('alsjdadask')
    log.log_close()