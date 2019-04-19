import Tasks
from Tasks import Tasks
import User
from User import User

class Board:
    taskList = []

    def createTask(self, name, state, u):
        newTask = Tasks(name, state, 0)
        newTask.user = User(u)
        self.taskList.append(newTask)

    def editTask(self):
        taskToEdit = input("Enter the exact name of the task to be edited:" )
        for task in self.taskList:
            if task.taskName == taskToEdit:
                task.taskName = input("Enter the new name of the task: ")
                task.taskStatus = input("What is the new status of the project(Assigned/Progress/Done): ")
                newTaskUser = input("Enter the user assigned to the project: ")
                task.user = User(newTaskUser)

    def deleteTask(self, taskToDelete):
        for task in self.taskList:
            if task.taskName == taskToDelete:
                taskList.remove(task)
                print ("Delete successful")

#changes to output format of board also need to be changed in task class            
    def getBoard(self):
        retString = "Task name - Assignee - Status" + '\n'
        for task in self.taskList:
            retString += task.getTask()
            retString += '\n'

        return retString
