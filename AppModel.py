import datetime
import json
from Task import Task

class AppModel:
    def __init__(self):
        self.prefDateFmt = "mm/dd/yy"
        self.datetimeFmtRegex = "%m/%d/%y"
        self.currentDate = datetime.MINYEAR
        self.taskFileName = "./data/tasks.json"
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

    def getTaskData(self, taskStr):
        taskList = self.getTaskList()
        for task in taskList:
            if task.title.upper() == taskStr:
                return (True, task)
        return (False, None)