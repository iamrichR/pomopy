from AppView import AppView
from AppModel import AppModel

class AppController:
    def __init__(self):
        self.view = AppView()
        self.model = AppModel()
        self.quitCommands = ["QUIT", "Q", "EXIT"]
        self.yesCommands = ["YES, Y"]
        self.noCommands = ["NO, Y"]

    def start(self):
        self.dailyLog()

    def dailyLog(self):
        quit = False
        while not quit:

            #TODO:  refactor date, task, quantity prompts into separate controller methods
            #TODO:  date entry should be BEFORE the loop

            #prompt date
            dateStr = self.view.promptDate(self.model.getPrefDateFmt())
            self.checkForQuit(dateStr)
            while not (self.model.isDateValid(dateStr)):
                self.view.showInputError(dateStr)
                dateStr = self.view.promptDate(self.model.getPrefDateFmt())
                self.checkForQuit(dateStr)
            
            #prompt task
            #TODO:  allow user to print tasklist if they want
            taskStr = self.view.promptTask()
            self.checkForQuit(taskStr)
            taskExists = self.model.checkForTask(taskStr)
            if not (taskExists):
                self.view.errTaskNotFound()
                #TODO:  allow user to either return to task entry or create new task
                #TODO:  make a separate logic flow to account for creation of new tasks

            
            quantitySet = False
            while not(quantitySet):
                try:
                    inputStr = self.view.promptQuantity(self.model.getCurrentTask().title, self.model.getCurrentDate())
                    quantity = int(inputStr)
                    quantitySet = True
                except ValueError:
                    self.view.showInputError(inputStr)

            #TODO:  check for successful log and print a success or failure message
            self.model.storeDailyLog(quantity)
            self.model.resetDailyLogValues()

            #add validation later, response should be either YES/Y or NO/N
            more = self.view.promptDailyLogContinue(self.model.getCurrentDate())

            self.checkForQuit(more)

            if more in self.noCommands:
                #TODO:  this doesn't seem to be working properly
                exit()


            #TODO:  loop daily log until user is done with that day



    def checkForQuit(self, inputStr):
        if inputStr in self.quitCommands:
            exit()

