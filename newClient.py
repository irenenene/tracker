import socket
#the string sent to the server will always start with a number so the server
#knows what type of command is issued
#format: number|option|option|etc.
#server will call different functions according to the number in token [0]

##### Function Definitions #####

def mainMenu():
    print("Main Menu")
    print("0. Exit")
    print("1. Enter a new task")
    print("2. Edit an existing task")
    print("3. Delete a task")
    print("4. Start/Stop work")
    print("5. View details")
    print("10. View the task board")

#returns a string to be encoded and sent to the server // should change this method
def addTask():
    tName = input("Enter the name of the task: ")
    tUser = input("Enter the name of the user assigned to the task:")
    retString = "1|" + tName + '|' + tUser
    return retString

def editTask():
     tName = input("Enter the name of the task: ")
     sendStr = "9|" + tName
     s.send(sendStr.encode())
     #displaying the task to be edited
     recvString = s.recv(port).decode()
     print(recvString)
     newName = input("Enter a new name: ")
     newUser = input("Enter a new user: ")
     sendStr = "8|" + tName + '|' + newName + '|' + newUser
     s.send(sendStr.encode())
     print("Done.")

def startStop():
    tName = input("Enter the name of the task: ")
    sendStr = "4|" + tName
    s.send(sendStr.encode())

def delTask():
    print("not implemented yet. should be ez as checking a name.")

##### End Function Definitions #####

s = socket.socket()
port = 6789
s.connect(("127.0.0.1", port))
userInput = "init"

while userInput != "exit":
    print("Welcome.")
    mainMenu()
    userInput = input("Please enter the number corresponding to your choice: ")
    if userInput == "0":
        print("Goodbye")
        s.send("0".encode())
        s.close()
        break
    elif userInput == "1":
        s.send(addTask().encode())
    elif userInput == "2":
        editTask()
    elif userInput == "3":
        delTask()
    elif userInput == "4":
        startStop()
    elif userInput == "10":
        sendString = "10"
        s.send(sendString.encode())
        recvString = s.recv(port).decode()
        print(recvString)
