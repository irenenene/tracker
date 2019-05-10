import socket
import datetime

#the string sent to the server will always start with a number so the server
#knows what type of command is issued
#format: number|option|option|etc.
#server will call different functions according to the number in token [0]

##### Function Definitions #####

def mainMenu():
    print("1. New | 2. Edit | 3. Delete | 4. Start Timer | 5. View All | 6. View Users | 0. Exit")


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
     sendStr = "2|" + tName + '|' + newName + '|' + newUser
     s.send(sendStr.encode())
     print("Done.")

def startStop():
    tName = input("Enter the name of the task: ")
    sendStr = "4|" + tName
    s.send(sendStr.encode())
    print("Done.")

def delTask():
    tName = input("Enter the name of the task: ")
    sendStr = "3|" + tName
    s.send(sendStr.encode())
    print("Done.")

##### End Function Definitions #####

print("Welcome.")
username = input("Enter your username: ")

s = socket.socket()
port = 6789
s.connect(("127.0.0.1", port))
s.send(username.encode())
userInput = "init"

# "1. New | 2. Edit | 3. Delete | 4. Start Timer | 5. View Tasks | 6. View Users | 0. Exit

while userInput != "0":
    now = datetime.datetime.now()
    print (now.strftime("%A %B %d"))

    mainMenu()
    userInput = input("Your selection: ")
    userInput = userInput.lower()
    userInput = userInput.strip()

    if userInput == "0" or userInput == "exit":
        print("Goodbye")
        s.send("0".encode())
        s.close()
        break
    elif userInput == "1" or userInput == "new":
        s.send(addTask().encode())
    elif userInput == "2" or userInput == "edit":
        editTask()
    elif userInput == "3" or userInput == "delete":
        delTask()
    elif userInput == "4" or userInput == "start timer":
        startStop()
    elif userInput == "5" or userInput == "view tasks":
        sendString = "10"
        s.send(sendString.encode())
        recvString = s.recv(port).decode()
        print(recvString)
        print("-----------")
    elif userInput == "6" or userInput == "view users":
        sendString = "6"
        s.send(sendString.encode())
        recvString = s.recv(port).decode()
        print("--Current Users--")
        print(recvString)
    else:
        print("Invalid Selection")
