'''from time import sleep, ctime
import threading

loops = [4,2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('ALL DONE at:', ctime())

if __name__ == '__main__':
    main()'''

'''import urllib.request
import lxml.html

u = urllib.request.Request('http://www.baidu.com')
print(type(u))
l = lxml.html.fromstring(str(u))

print(lxml.html.tostring(l,pretty_print=True))
'''

from myThread import MyThread
from time import ctime, sleep

def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x - 1))

def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x - 1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))
    print('*** SINGLE THREAD')
    for i in nfuncs:
        print('Starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime(), '\n')

    print('\n*** MULTIPLE THREADS')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__ )
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
    print('ALL DONE')

if __name__ == '__main__':
    main()