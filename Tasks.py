import User
from User import User

import datetime
class Tasks:
    def __init__(self, taskName, taskStatus):
        #Default variables to be printed
        self.taskName = taskName
        self.taskStatus = taskStatus
        #taskStatus can be of the following: incomplete, complete, or moved
        #status can also just be an event or a note.
        self.user = None

        #Variables used during time logging
        self.startTime = None
        self.endTime = None
        self.timeSpent = None
        self.active = False

    def getSymbol(self):
        #returns the appropriate symbol for taskStatus
        if self.taskStatus == "incomplete":
            return '-'
        elif self.taskStatus == "complete":
            return 'x'
        elif self.taskStatus == "moved":
            return '>'
        elif self.taskStatus == "event":
            return '*'
        elif self.taskStatus == "note":
            return '~'
        else
            return ' '

    def getTask(self):
        #Returns a string with the task info
        retString = '\t' + self.getSymbol() + ' ' + self.taskName
        if self.user:
            retString += " \\\\ " + self.user.name

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
