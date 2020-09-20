import datetime
import json
from Task import Task
from PomoLog import PomoLog

class AppModel:
    def __init__(self):
        self.prefDateFmt = "mm/dd/yy"
        self.datetimeFmtRegex = "%m/%d/%y"
        self.taskFileName = "./data/tasks.json"
        self.logFileName = "./data/logs.dat"
        self.currentDate = datetime.datetime.today()
        self.currentTask = None
        self.currentQuantity = 0
        #TODO:  Save taskList as a class variable and keep it updated instead of retrieving it over and over.

    def isDateValid(self, dateStr):
        try:
            self.currentDate = datetime.datetime.strptime(dateStr, self.datetimeFmtRegex)
            return True
        except ValueError:
            return False
    
    def getCurrentDate(self):
        return self.currentDate.strftime(self.datetimeFmtRegex)

    def getPrefDateFmt(self):
        return self.prefDateFmt

    def setCurrentQuantity(self, quantity):
        self.currentQuantity = quantity

    def getCurrentQuantity(self):
        return self.currentQuantity

    def getTaskList(self):
        taskList = []
        taskFile = open(self.taskFileName)
        for line in taskFile:
            newTaskData = line.strip().split("|")
            title = newTaskData[0].strip()
            tags = json.loads(newTaskData[1].strip())
            newTask = Task(title, tags)
            taskList.append(newTask)
        taskFile.close()
        return taskList

    def checkForTask(self, taskStr):
        taskList = self.getTaskList()
        for task in taskList:
            if task.title.upper() == taskStr:
                self.currentTask = task
                return True
        return False

    def getCurrentTask(self):
        return self.currentTask

    def storeDailyLog(self):
        log = PomoLog(self.currentDate, self.currentTask, self.currentQuantity)
        #TODO:  implement a better storage solution later, with JSON(?)
        logFile = open(self.logFileName, 'a')
        logFile.write(str(log) + "\n")
        logFile.close()

    def resetDailyLogValues(self):
        self.currentTask = None
        self.currentQuantity = 0

    def resetDate(self):
        self.currentDate = datetime.datetime.today()