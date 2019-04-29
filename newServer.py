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
            taskBoard.createTask(tokenList[1], "incomplete", tokenList[2])
        elif tokenList[0] == "0":
            clientSock.close()
            print("Closing connection")
            break
        elif tokenList[0] == "3":
            taskBoard.deleteTask(tokenList[1])
        elif tokenList[0] == "4":
            taskBoard.logTime(tokenList[1])
        elif tokenList[0] == "8":
            taskBoard.editTask(tokenList[1], tokenList[2], tokenList[3])
        elif tokenList[0] == "9": #find
            retString = taskBoard.findTask(tokenList[1])
            clientSock.send(retString.encode())
        elif tokenList[0] == "10":
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
