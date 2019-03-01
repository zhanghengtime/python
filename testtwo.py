'''import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.errno , socket.gaierror ) as e:
        print 'ERROR : cannot rech "%s" ' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s"' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE ,open(FILE,'wb+').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Download "%s" to CWD' % FILE
    f.quit()

if __name__ == '__main__':
    main()'''

# CrowTaobaoPrice.py
import requests
import re
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        return demo
    except:
        return ""


def parsePage(ilt, demo):
    try:
        soup = BeautifulSoup(demo, 'html.parser')
        for line in soup.find_all('span'):
            price = line.get("search_now_price")
            title = line.get("skcolor_ljg")
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format(" 序号", " 价格", "   商品名称    "))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = input('Please in put a goods: ')
    #depth = 6
    start_url = 'http://search.dangdang.com/?key=' + goods
    infoList = []
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(start_url, timeout=30, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    title = []
    ilt = []
    price = []
    soup = BeautifulSoup(demo, 'html.parser')
    for line in soup.find_all('p', "price"):
        price.append(line.span.string)
    for line in soup.find_all('p', "name"):
        s = line.a.get('title')
        titles = s.split(' ')
        title.append(titles[1])
        print(titles[1])
    for i in range(len(titles)):
        ilt.append([price[i], title[i]])
    print(ilt)
    print(len(title))
    print(len(price))
    #for i in range(depth):
     #   try:
      #      url = start_url + '&page_index=' + i
       #     html = getHTMLText(url)
        #    parsePage(infoList, html)
        #except:
         #   continue
    #printGoodsList(infoList)

if __name__ == '__main__':
    main()





