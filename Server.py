import socket

s = socket.socket()
print ("Socket created")

port = 6789
ipAddr = '' # Empty string - listening for hosts on the local network

s.bind((ipAddr, port))
print ("socket bound to %s" %(port))

# listen for up to 5 hosts on the socket
s.listen(5)
print ("socket is listening")

# socket.accept() returns a value of (conn, address)
# conn is a new socket object
# address is the address bound to the socket on the other end
while True:
    c, addr = s.accept() #accept will block until a connection is created

    #you will want to create a separate thread to service client requests
    
    print ("Got connection from", addr)

    sendString = "Hello there"
    
    c.send(sendString.encode())

    c.close()
