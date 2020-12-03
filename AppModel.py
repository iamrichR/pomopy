import datetime
import json
import os
from Task import Task
from PomoLog import PomoLog
from FileManager import FileManager

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
        self.fileManager = FileManager()
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
        (listName, taskList) = self.fileManager.fetchJSONList(self.taskFileName)
        return taskList

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
        self.fileManager.addItemtoList(self.taskFileName, newTask.getData())
        
    def addTagtoTask(self, title, tag):
        taskList = self.getTaskList()
        for task in taskList:
            if(task['title'] == title):
                task['tags'].append(tag)
        self.fileManager.updateList(self.taskFileName, taskList)

    #TODO:  instead of providing literal filename to this method, have the method take a date and find the appropriate logfile
    def getLogList(self):
        (listName, logList) = self.fileManager.fetchJSONList(self.getLogFileName())
        return logList

    def createNewDailyLog(self):
        log = PomoLog(
            self.currentDate.strftime("%m/%d/%y"), 
            self.currentTask.getData(), 
            self.currentQuantity)
        self.fileManager.addItemtoList(self.getLogFileName(), log.__dict__, "logs")

    def resetDailyLogValues(self):
        self.currentTask = None
        self.currentQuantity = 0

    def resetDate(self):
        self.currentDate = datetime.datetime.today()





if __name__ == "__main__":

    def testCreateNewTask():
        model = AppModel()
        length = len(model.getTaskList())
        print(len(model.getTaskList()))
        model.createNewTask("test_1", "tag1")
        model.createNewTask("test_2", "tag2")
        newLength = len(model.getTaskList())
        print(len(model.getTaskList()))
        if length+2 == (newLength):
            print("test successful")
        else:
            print("test failed")

    testCreateNewTask()