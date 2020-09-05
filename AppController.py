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

            #TODO:  Implement taskList in model
            #TODO:  check taskStr against taskList in model

    def checkForQuit(self, inputStr):
        if inputStr.upper() in self.quitCommands:
            exit()

