import datetime
import json
from PomoLog import PomoLog
from Task import Task

taskFileStr = './tasks.json'

## functions ##

# prompt function
def promptLog(date):
    title = input("Please enter a title for the task.\n").lower()

    task = createTask(title)

    quantity = int(input("\nPlease enter the number of pomodoros spent on\nthis task on %s\n" %date))

    log = PomoLog(date, quantity, task)

    return log


def createTask(title):
    taskFile = open(taskFileStr)
    tasks = taskFile.readlines()
    taskFile.close()

    taskIndex = taskExists(title, tasks)

    if(taskIndex):
        return tasks[taskIndex]
    else:
        tags = promptTags()
        newTask = Task(title, tags)
        taskFileUpdate = open(taskFileStr, 'a')
        taskFileUpdate.write('\n' + str(newTask))
        taskFileUpdate.close()
        return newTask

    #return task


def taskExists(title, tasks):
    for idx, task in enumerate(tasks):
        if title in task:
            return idx
    
    return False


def promptTags(tags=[]):
    nextTag = (input("\nPlease enter a short tag labeling this task\n"))
    
    if(nextTag != ''):
        tags.append(nextTag.lower())
        tags = promptTags(tags)

    return tags




## main ##
dateStr = input("Please enter the date to be logged\nmm/dd/yy format\n")
date = datetime.datetime.strptime(dateStr, '%m/%d/%y')
jsonData = "{\n"

print("\n")
#jsonData += json.dumps(promptLog(date)) + ","
jsonData += str(promptLog(date)) + "\n"

more = input("\nDo you want to log another task for %s?\n" %dateStr)[0].upper()

while(more != "N"):
    print("\n")
    #jsonData += json.dumps(promptLog(date)) + ","
    jsonData += str(promptLog(date)) + "\n"
    more = input("\nDo you want to log another task for %s?\n" %dateStr)[0].upper()

jsonData += "}"

filename = "pomos.txt"
writeFile = open(filename, "w")

writeFile.write(jsonData)


input("\nexiting program...")