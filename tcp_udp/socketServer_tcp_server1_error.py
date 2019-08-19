 #encoding=utf-8
#创建一个socketserverTCP服务器
#高级模块，简化客户和服务器的实现
from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

host = ''
port = 9999
addr = (host,port)

#从 SocketServer 的 StreamRequestHandler 类中派生出一个子类
class MyRequestHandler(SRH):
    def handel(self):
        print('connected from ',self.client_address)
        self.wfile.write('[%s] %s ' % (ctime(),self.rfile.readline()))
        #用 readline()函数得到客户消息，用 write()函数把字符串发给客户。

tcpServ = TCP(addr,MyRequestHandler)
print('waiting for connection')
tcpServ.serve_forever()