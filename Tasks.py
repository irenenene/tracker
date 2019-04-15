import User
from User import User

class Tasks:
    def __init__(self, taskName, taskStatus, timeSpent):
        self.taskName = taskName
        self.taskStatus = taskStatus
        self.timeSpent = timeSpent
        self.user = User("Unassigned")
		
    def getTask(self):
        return self.taskName + ' - ' + self.user.name + ' - ' + self.taskStatus
