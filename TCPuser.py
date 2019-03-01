"""import socket
from socket import *
target_host = "127.0.0.1"
target_port = 1024


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',21567))

while True:
    data = raw_input('please:')
    if data == 'quit':
        break
    if data == '':
        continue
    client.send(data.encode())
    print (client.recv(1024).decode('utf-8'))
client.send(b'quit')
client.close()

"""
"""
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("www.baidu.com",80))

client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

response = client.recv(4096)

print response
"""
'''
while True:

    client = socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.1',21568))
    data = raw_input('>')
    if not data:
        break
    client.send('%s\r\n' % data)
    data = client.recv(target_port)
    if not data:
        break
    print data.strip()
    client.close()'''

import time
import queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print("Connect to server %s..."%server_addr)
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n,n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
print('worker exit.')
