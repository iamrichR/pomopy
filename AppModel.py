import datetime
import json
from os import path
from Task import Task
from PomoLog import PomoLog

class AppModel:
    def __init__(self):
        self.prefDateFmt = "mm/dd/yy"
        self.datetimeFmtRegex = "%m/%d/%y"
        self.dataPath = "./data/"
        self.taskFileName = self.dataPath+"tasks.json"
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

    def getLogFileName(self):
        return self.dataPath+(self.currentDate.strftime("%y%m%d")+"-pomo_log.json")

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

    def createNewTask(self, title, tag):
        newTask = Task(title, [tag])
        #TODO:  change all file open/close statements to the "with..as" format, it's cleaner.
        taskFile = open(self.taskFileName,'a')
        taskFile.write(json.dumps(newTask.getData()) + "\n")
        taskFile.close()

    def addTagtoTask(self, title, tag):
        #TODO:  open file and readlines, edit the line you need to edit, then rewrite all data back into the file.

    def storeDailyLog(self):
        log = PomoLog(self.currentDate, self.currentTask, self.currentQuantity)
        #TODO:  implement a better storage solution later, with JSON(?)
        logfileName = self.getLogFileName()
        logFile = open(logfileName, 'a')
        logFile.write(json.dumps(log.getData()) + "\n")
        #logFile.write(str(log) + "\n")
        logFile.close()

    def resetDailyLogValues(self):
        self.currentTask = None
        self.currentQuantity = 0

    def resetDate(self):
        self.currentDate = datetime.datetime.today()