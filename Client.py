import socket
import threading

##def Listener(sock, stopped):
##    while True:
##        print ("From server: ")
##        print (sock.recv(port).decode())
##        if stopped():
##            break
##    print("Exiting thread")
##
##def Sender(sock, stopped):
##    userInput = "Go"
##    while userInput != "exit":
##        userInput = input()
##        s.send(userInput.encode())
##    stopped = True;
        

s = socket.socket()
isExit = False
port = 6789
stopped = False

s.connect(("127.0.0.1", port))

##listenThread = threading.Thread(target=Listener, args=(s, lambda: stopped))
##listenThread.start()
##sendThread = threading.Thread(target=Sender, args=(s, lambda: stopped))
##sendThread.start()

while True:
    print (s.recv(port).decode())
    userInput = input()
    s.send(userInput.encode())

s.close()
