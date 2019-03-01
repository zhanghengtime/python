from twisted.internet import protocol , reactor

HOST = 'localhost'
PORT = 21567

class TSClntprotocol(protocol.ProcessProtocol):
    def sendData(self):
        data = raw_input('>')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self,data):
        print data
        self.sendData()

class TSCintFactory(protocol.ClientFactory):
    protocol = TSClntprotocol
    clientConnectionLost = clientConnectionFailed = lambda self , connector ,reason : reactor.stop()

reactor.connectTCP(HOST,PORT,TSCintFactory())
reactor.run()
