import socket
import Board
from Board import Board
import threading

def userInteract(sock):
    contents = theBoard.getBoard()
    sock.send(b"Welcome.")
      
    
    sInput = "Go"

    while sInput != "exit":
        sOutput = "Press 1 to enter a new task, 2 to edit an existing task, and 3 to delete task: "
        sock.send(sOutput.encode())
        
        sInput = sock.recv(port).decode()
        
        if sInput == "1":
            sOutput = "Enter the name of the task: "
            sock.send(sOutput.encode())
            newTaskName = sock.recv(port).decode()

            sOutput = "Enter the status of the task: (eg. Done) "
            sock.send(sOutput.encode())
            newTaskStatus = sock.recv(port).decode()

            sOutput = "Enter the user assigned to the project: "
            sock.send(sOutput.encode())
            newTaskUser = sock.recv(port).decode()

            theBoard.createTask(newTaskName, newTaskStatus, newTaskUser)          
            
        if sInput == "2":
            print("Not implemented yet")
        if sInput == "3":
            print("Not implemented yet")

        contents = theBoard.getBoard()
        sock.send(contents.encode())
    
    print("Thread finished")
    sock.close()

# # # # #

theBoard = Board()
socketList = []

s = socket.socket()
print ("Socket created")

port = 6789
ipAddr = '127.0.0.1' # localhost
s.bind((ipAddr, port))
print ("socket bound to %s" %(port))

# listen for up to 5 hosts on the socket
s.listen(5)
print ("socket is listening")

# socket.accept() returns a value of (conn, address)
# where conn is a new socket object
# address is the address bound to the socket on the other end
while True:
    c, addr = s.accept() # accept will block until a connection is created
    #c.setblocking(False)
    socketList.append(c)
    
    # you will want to create a separate thread to service client requests    
    print ("Got connection from", addr)
    newThread = threading.Thread(target=userInteract, args=(c,))
    newThread.start()
