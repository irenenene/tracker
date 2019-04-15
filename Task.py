import User
from User import User

class Task:
    def __init__(self, taskName):
        self.name = taskName
        self.user = User("Unassigned")
        #self.dueDate
        #self.category
        #

    def printTask(self):
           print(self.name, ' - ', self.user.name)
