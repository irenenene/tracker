import socket
import Board
from Board import Board
import threading

def userInteract(sock):
    contents = theBoard.getBoard()
    sock.send(contents.encode())
    print("Thread finished")
    c.close()

theBoard = Board()
#socketList = []

s = socket.socket()
print ("Socket created")

port = 6789
ipAddr = '127.0.0.1' # Empty string - listening for hosts on the local network
s.bind((ipAddr, port))
print ("socket bound to %s" %(port))

# listen for up to 5 hosts on the socket
s.listen(5)
print ("socket is listening")

# socket.accept() returns a value of (conn, address)
# where conn is a new socket object
# address is the address bound to the socket on the other end
while True:
    c, addr = s.accept() #accept will block until a connection is created
#    socketList.append(c)
    
    # you will want to create a separate thread to service client requests    
    print ("Got connection from", addr)
    newThread = threading.Thread(target=userInteract, args=(c,))
    newThread.start()
