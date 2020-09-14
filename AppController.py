from AppView import AppView
from AppModel import AppModel

class AppController:
    def __init__(self):
        self.view = AppView()
        self.model = AppModel()
        self.quitCommands = ["QUIT", "Q", "EXIT"]

    def start(self):
        self.dailyLog()

    def dailyLog(self):
        quit = False
        while not quit:
            #prompt date
            dateStr = self.view.promptDate(self.model.getPrefDateFmt())
            self.checkForQuit(dateStr)
            while not (self.model.isDateValid(dateStr)):
                self.view.showInputError(dateStr)
                dateStr = self.view.promptDate(self.model.getPrefDateFmt())
                self.checkForQuit(dateStr)
            
            #prompt task
            taskStr = self.view.promptTask()
            self.checkForQuit(taskStr)
            if(self.model.taskAlreadyExists(taskStr)):
                taskData = self.model.getTaskData(taskStr)
                print(taskData)
            else:
                print("whoops couldn't find that task")
                #TODO:  Make this a view method

            #TODO:  make a separate logic flow to account for creation of new tasks
            
            #TODO:  once task is determined, prompt quantity

            #TODO:  continue converting dailylog, next step is creating PomoLog object and storing


    def checkForQuit(self, inputStr):
        if inputStr.upper() in self.quitCommands:
            exit()

