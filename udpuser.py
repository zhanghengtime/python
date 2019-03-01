'''import socket

target_host = '127.0.0.1'
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto("Hello!",(target_host,target_port))

data , addr = client.recvfrom(36442)

print (data)'''


import requests
import re
from bs4 import BeautifulSoup
import bs4

def getHTMlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(tplt.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(' '+u[0],u[1],u[2],chr(12288)))

def main():
    unifo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMlText(url)
    fillUnivList(unifo,html)
    num = input('Please input a number: ')
    num = int(num)
    printUnivList(unifo,num)

if __name__ == '__main__':
    main()


