#from socket import *
from time import ctime
"""
HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpsersock = socket(AF_INET,SOCK_STREAM)
tcpsersock.bind(ADDR)
tcpsersock.listen(5)

while True:
    print 'waiting for connecting...'
    tcpclisock , addr = tcpsersock.accept()
    print '...connecting from:' ,addr

    while True:
        try:
            data = tcpclisock.recv(BUFSIZ)
            if not data:
                break
            tcpclisock.send('[%s] %s' % (ctime(),data))
        except:
            break
    if data == 'quit':
        break
    tcpclisock.close()
tcpsersock.close()
print 'closed!'

"""
from SocketServer import (TCPServer as TCP ,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21568
ADDR = (HOST,PORT)

class Myrequesthandler(SRH):
    def handle(self):
        print '...connectted from:' , self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))

tcpserv = TCP(ADDR,Myrequesthandler)
print 'waiting for connecting...'
tcpserv.serve_forever()