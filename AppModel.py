import datetime
import json
import os
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
            return jsonData
        except ValueError:
            return None

    def updateFile(self, path, data):
        with open(path, 'w') as writeFile:
            writeFile.write(data)

    def getTaskList(self):
        fileData = self.getJSONDataFromFile(self.taskFileName)
        if(isinstance(fileData, dict) and 'taskList' in fileData):
            taskList = fileData['taskList']
            return taskList
        else:
            return None

    def updateTaskData(self, newTaskList):
        self.updateFile(self.taskFileName, json.dumps({"taskList":newTaskList}))

    def checkForTask(self, taskStr):
        taskList = self.getTaskList()
        if taskList is not None:
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
        oldTaskList = self.getTaskList()
        if oldTaskList is None:
            newTaskList = [task.getData()]
        else:
            newTaskList = oldTaskList + [(task.getData())]
        self.updateTaskData(newTaskList)

    def addTagtoTask(self, title, tag):
        taskList = self.getTaskList()
        for task in taskList:
            if(task['title'] == title):
                task['tags'].append(tag)
        
        self.updateTaskData(taskList)

    #TODO:  instead of providing literal filename to this method, have the method take a date and find the appropriate logfile
    def getLogList(self):
        path = self.getLogFileName()
        if(os.path.exists(path)):
            fileData = self.getJSONDataFromFile(path)
            logData = fileData['logs']
            return logData
        else:
            return None

    def updateDateLog(self, logData):
        self.updateFile(self.getLogFileName(), json.dumps({"logs":logData}))

    def createNewDailyLog(self):
        log = PomoLog(
            self.currentDate.strftime("%m/%d/%y"), 
            self.currentTask.getData(), 
            self.currentQuantity)
        self.storeDailyLog(log)

    #TODO:  update storeDailyLog() to match how taskFile updating is happening
    def storeDailyLog(self, log):
        logData = log.__dict__
        oldLogList = self.getLogList()
        if(oldLogList is None):
            newLogList = [logData]
        else:
            newLogList = oldLogList + [logData]
        self.updateDateLog(newLogList)

    def resetDailyLogValues(self):
        self.currentTask = None
        self.currentQuantity = 0

    def resetDate(self):
        self.currentDate = datetime.datetime.today()





# if __name__ == "__main__":
#     model = AppModel()
#     newTask1 = Task("test_1", ["tag1", "shared-tag"])
#     newTask2 = Task("test_2", ["tag1", "shared-tag"])
#     model.storeNewTask(newTask1)
#     model.storeNewTask(newTask2)