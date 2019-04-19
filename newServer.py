import socket
import Board
from Board import Board
import threading
import time

def clientHandler(clientSock):
    while True:
        clientIn = clientSock.recv(port).decode()
        tokenList = clientIn.split("|")
        if tokenList[0] == "1":
            taskBoard.createTask(tokenList[1], "To-Do", tokenList[2])
        if tokenList[0] == "0":
            clientSock.close()
            print("Closing connection")
            break
        if tokenList[0] == "10":
            contents = taskBoard.getBoard()
            clientSock.send(contents.encode())


taskBoard = Board()
socketList = []

serverSock = socket.socket()
port = 6789
ipAddr = "127.0.0.1"
serverSock.bind((ipAddr, port))
serverSock.listen(5)
print("socket is listening")

while True:
    c, addr = serverSock.accept()
    socketList.append(c)
    print("Got connection from", addr)
    newThread = threading.Thread(target=clientHandler, args=(c,))
    newThread.start()
