import Tasks
from Tasks import Tasks
import User
from User import User

class Board:
    taskList = []
	
    #prompt the user for task name, task status, and current username
    #returns the newly created task
    def createTask(self, name, state, u):
        # newTask = Tasks()
        # newTaskName = input("Enter the name of the task: ")
        # newTaskStatus = input("Enter the status of the task(Assigned/Progress/Done): ")
        # newTaskTime = 0
        # newTaskUser = input("Enter the user assigned to the project: ")
        # newTask.taskName = newTaskName
        # newTask.taskStatus = newTaskStatus
        # newTask.timeSpent = newTaskTime
        # newTask.user = User(newTaskUser)
        # return newTask
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

    def deleteTask(self):
        taskToDelete = input("Enter the exact name of the task to be deleted: ")
        for task in self.taskList:
            if task.taskName == taskToDelete:
                taskList.remove(task)
                print ("Success")
				
    def masterControl(self, ans):
        ans = input("Press 1 to enter a new task, 2 to edit an existing task, and 3 to delete task: ")
        if ans == "1":
            task = self.createTask()
            self.taskList.append(task)
        if ans == "2":
            self.edit(taskList)
        if ans == "3":
            self.deleteTask(taskList)
			
    def getBoard(self):
        retString = "Task name - Assignee - Status" + '\n'
        for task in self.taskList:
            retString += task.getTask()
            retString += '\n'

        return retString