import datetime
import json
from os import path
from Task import Task
from PomoLog import PomoLog

#TODO:  change all file open/close statements to the "with..as" format, it's cleaner.

class AppModel:
    def __init__(self):
        self.prefDateFmt = "mm/dd/yy"
        self.datetimeFmtRegex = "%m/%d/%y"
        self.dataPath = "./data/"
        #TODO:  if tasks.json file does not exist, set it up
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

    def getJSONDataFromFile(self, path):
        with open(path, 'r') as dataSource:
            data = dataSource.read()
        try:
            jsonData = json.loads(data)
            return jsonData[]
        except ValueError:
            return None

    def updateFile(self, path, data):
        with open(path, 'w') as writeFile:
            writeFile.write(data)

    def appendFile(self, path, data):
        with open(path, 'a') as appendFile:
            appendFile.write(data)

    def getTaskList(self):
        fileData = self.getJSONDataFromFile(self.taskFileName)
        tasklist = fileData['taskList']
        return taskList

    def updateTaskData(self, newTaskList):
        self.updateFile(self.taskFileName, json.dumps(newTaskList))

    def checkForTask(self, taskStr):
        taskList = self.getTaskList()
        for task in taskList:
            if task['title'] == taskStr:
                return Task(task['title'], task['tags'])
        return None

    def setCurrentTask(self, task):
        self.currentTask = task

    def getCurrentTask(self):
        return self.currentTask

    def createNewTask(self, title, tag):
        newTask = Task(title, [tag])
        self.storeNewTask(newTask)
        

    def storeNewTask(self, task):
        newTaskList = self.getTaskList().append(task.getData)

        self.updateTaskData(newTaskList)

    def addTagtoTask(self, title, tag):
        taskList = self.getTaskList()

        for task in taskList:
            if(task['title'] == title):
                task['tags'].append(tag)
        
        self.updateTaskData(taskList)

    #TODO:  instead of providing literal filename to this method, have the method take a date and find the appropriate logfile
    def getLogData(self, path):
        fileData = self.getJSONDataFromFile(path)
        logData = fileData['logData']
        return logData

    def updateDateLog(self, log):
        logfileName = self.getLogFileName()
        self.appendFile(logfileName, json.dumps(log))

    #TODO:  update storeDailyLog() to match how taskFile updating is happening
    def storeDailyLog(self):
        log = PomoLog(self.currentDate, self.currentTask, self.currentQuantity)
        logfileName = self.getLogFileName()
        with open(logfileName, 'a') as logFile:
            logFile.write(json.dumps(log.getData()) + "\n")

    def resetDailyLogValues(self):
        self.currentTask = None
        self.currentQuantity = 0

    def resetDate(self):
        self.currentDate = datetime.datetime.today()