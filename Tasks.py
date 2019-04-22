import User
from User import User
<<<<<<< HEAD:Tasks.py

=======
import datetime
>>>>>>> bbaf0d2c49cc77cd31e65ba2a7c2b02a1a309100:Tasks
class Tasks:
    def __init__(self, taskName, taskStatus, startTime, endTime, timeSpent):
        self.taskName = taskName
        self.taskStatus = taskStatus
        self.startTime = startTime
        self.endTime = endTime
        self.timeSpent = timeSpent
        self.user = User("Unassigned")
<<<<<<< HEAD:Tasks.py
		
    def getTask(self):
        return self.taskName + ' - ' + self.user.name + ' - ' + self.taskStatus
=======
    def startWorkTime(self):
        self.startTime = datetime.datetime.now()
        return self.startTime
    def endWorkTime(self):
        self.endTime = datetime.datetime.now()
        return self.endTime
    def totalTimeWorked(self,startTime, endTime):
        deltaTime = endTime-startTime
        secs = deltaTime.total_seconds()
        hoursWorked = secs/3600
        minWorked = (secs%3600)/60
        decMinWorked = minWorked/60
        self.timeSpent = self.timeSpent + hoursWorked + decMinWorked
        return format(self.timeSpent, '.2f')
>>>>>>> bbaf0d2c49cc77cd31e65ba2a7c2b02a1a309100:Tasks
