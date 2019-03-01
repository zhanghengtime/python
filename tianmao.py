from random import randint
from myThread import MyThread
from time import sleep
from queue import Queue
import concurrent.futures

def writeQ(queue):
    print('producting object for Q...',end='')
    queue.put('xxx')
    print('size now', queue.qsize())

def readQ(queue):
    queue.get()
    print('consumed object from Q... size now', queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    queue = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (queue, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')

if __name__ == '__main__':
    main()