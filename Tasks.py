import User
from User import User

import datetime
class Tasks:
    def __init__(self, taskName, taskStatus):
        self.taskName = taskName
        self.taskStatus = taskStatus
        self.startTime = None
        self.endTime = None
        self.timeSpent = None
        self.user = None
        self.active = False

    def getTask(self):
        return self.taskName + ' - ' + self.user.name + ' - ' + self.taskStatus

    def startWorkTime(self):
        self.startTime = datetime.datetime.now()
        return self.startTime
    def endWorkTime(self):
        self.endTime = datetime.datetime.now()
        return self.endTime
    def totalTimeWorked(self, startTime, endTime):
        deltaTime = endTime-startTime
        secs = deltaTime.total_seconds()
        hoursWorked = secs/3600
        minWorked = (secs%3600)/60
        decMinWorked = minWorked/60
        self.timeSpent = self.timeSpent + hoursWorked + decMinWorked
        return format(self.timeSpent, '.2f')
