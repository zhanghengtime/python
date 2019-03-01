import socket
import time
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.bind(('127.0.0.1',10021))

client.listen(3)

print 'Server is running...'

def TCP(sock,addr):
    print 'Accept new connecion from %s:%s.' %addr
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode() == 'quit':
            break
        sock.send(data.decode('utf-8').upper().encode())
    sock.close()
    print 'Connection from %s:%s closed.' %addr

while True:
    sock,addr = client.accept()
    TCP(sock,addr)

