from socket import *
import traceback

HOST = 'localhost'  # or 'localhost'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
info = True
try:
    tcpCliSock.connect(ADDR)
except ConnectionRefusedError :
    print(traceback.format_exc())
    s = False


while info:
    data = input('> ')
    if not data:
        break

    tcpCliSock.send(data.encode("utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))

tcpCliSock.close()