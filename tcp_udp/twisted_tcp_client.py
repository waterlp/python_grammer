#!/usur/bin/env python
#-*- coding:UTF-8 -*-
from twisted.internet import protocol, reactor

HOST='localhost'
PORT=9999

class TSClntProtocol (protocol.Protocol):
    def sendData(self):
        data = input('> ').encode('utf-8')
        print(type(data))
        if data:
            print('...sending %s...'%data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self,data):
        print(data)
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()
