import Tasks
from Tasks import Tasks
import User
from User import User

class Board:
    taskList = []
    users = []

    def createTask(self, name, state, uname):
        newTask = Tasks(name, state)
        newTask.user = User(uname)
        self.taskList.append(newTask)

    def editTask(self, currname, newname, newuser):
        for t in self.taskList:
            if t.taskName == currname:
                t.taskName = newname
                #change the User. Will need to modify the way users are tracked
                #in this system.

    def deleteTask(self, taskToDelete):
        for task in self.taskList:
            if task.taskName == taskToDelete:
                self.taskList.remove(task)
                print ("Delete successful")
                break

#changes to output format of board also need to be changed in task class
    def getBoard(self):
        retString = "Task name - Assignee - Status" + '\n'
        for task in self.taskList:
            retString += task.getTask()
            retString += '\n'

        return retString

    def findTask(self, searchName):
        for t in self.taskList:
            if t.taskName == searchName:
                return t.getTask()
        return "Task not found."


    def logTime(self, tName):
        for t in self.taskList:
            if t.taskName == tName:
                if t.active:
                    t.endWorkTime()
                else:
                    t.startWorkTime()
