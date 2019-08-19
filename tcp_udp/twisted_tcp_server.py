#!/usur/bin/env python
#-*- coding:UTF-8 -*-
import twisted
from twisted.internet import protocol, reactor
from time import ctime

PORT=9999

class TSServProtocol (protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from :',clnt)
    def dataReceived(self,data):
        print(data)
        self.transport.write(('[%s] %s' % (ctime(),data)).encode())
        # self.transport.write(data)

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()
