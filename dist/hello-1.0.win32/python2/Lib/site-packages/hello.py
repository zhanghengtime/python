import socket

"""s = socket.socket()

host = socket.gethostname()
port = 24
s.bind((host,port))

s.listen(5)
while True:
    c,addr = s.accept()
    print 'Got connection from' , addr
    c.send('Thank you for connecting')
    c.close()

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host,port))
print s.recv(1024)"""

"""from SocketServer import TCPServer,ThreadingMixIn,StreamRequestHandler

class Server(ThreadingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write("Thanks you for connecting")

server = Server((host,1234),Handler)
server.serve_forever()"""

"""
from subprocess import Popen,PIPE
from urllib import urlretrieve

text = open('mess.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE,shell=True )
 #print tidy

tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read()"""

"""
from urllib import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h2':
            self.in_h3 = True

        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h2':
            self.in_h2 = False
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print '%s (%s)' % (''.join(self.chunks),self.url)
            self.in_link = False

text = urlopen('https://www.python.org/jobs').read()
parser = Scraper()
parser.feed(text)
parser.close() """

# from urllib import urlretrieve
# urlretrieve("https://www.python.org/jobs/","python job.html")

"""
from hello2 import area

heigth = 3
width = 4
correct_answer = 12
answer = area(heigth,width)
if correct_answer == answer:
    print 'correct!'
else:
    print "error!"

import profile
print profile.run('area(3,4)')
"""
"""
import unittest, hello2
from subprocess import Popen, PIPE


class ProductCase(unittest.TestCase):
    def tesWithPyLint(self):
        cmd = 'pylint', '-Q', hello2._file_.rstrip('c')
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')


if __name__ == '__main__':
    unittest.main()"""

from distutils.core import setup

setup(name='hello',version='1.0',description='A simple example',author='Magnus Lie Hetland',py_modules=['hello'])