from AppView import AppView
from AppModel import AppModel

class AppController:
    def __init__(self):
        self.view = AppView()
        self.model = AppModel()
        self.quitCommands = ["QUIT", "Q", "EXIT"]
        self.yesCommands = ["YES", "Y"]
        self.noCommands = ["NO", "N"]

    def start(self):
        #TODO:  make a main menu
        self.dailyLog()

    def dailyLog(self):
        quit = False

        self.getValidDateInput()

        while not quit:
            self.getValidTaskInput()
            self.getValidQuantityInput()

            #TODO:  check for successful log and print a success or failure message
            self.model.storeDailyLog()
            self.model.resetDailyLogValues()

            #add validation later, response should be either YES/Y or NO/N
            more = self.view.promptDailyLogContinue(self.model.getCurrentDate())

            self.checkForQuit(more)

            if more in self.noCommands:
                quit = True
        #TODO:V:  will eventually return to the main menu here, once there's a main menu
        print("\n**\nend of program\n**\n")

    def getValidDateInput(self):
            dateStr = self.view.promptDate(self.model.getPrefDateFmt())
            self.checkForQuit(dateStr)
            while not (self.model.isDateValid(dateStr)):
                self.view.showInputError(dateStr)
                dateStr = self.view.promptDate(self.model.getPrefDateFmt())
                self.checkForQuit(dateStr)

    def getValidTaskInput(self):
        #TODO:  allow user to print tasklist if they want
        taskStr = self.view.promptTask()
        self.checkForQuit(taskStr)
        existingTask = self.model.checkForTask(taskStr)
        if existingTask is None:
            self.view.errTaskNotFound()
            #TODO:  standard method to check Y/N input
            ynStr = self.view.promptNewTask(taskStr)
            if(ynStr in self.yesCommands):
                tagStr = self.view.promptTaskTags(taskStr)
                if len(tagStr) == 0:
                    self.view.errTagNeeded()
                self.model.createNewTask(taskStr, tagStr)
                tagStr = self.view.promptTaskTags(taskStr)
                while not (len(tagStr) == 0):
                    #TODO:  tasks should probably have numeric IDs for ease of use
                    self.model.addTagtoTask(taskStr, tagStr)
                    tagStr = self.view.promptTaskTags(taskStr)
                self.model.setCurrentTask(self.model.checkForTask(taskStr))
            else:
                print("hmmm")
                #TODO:  what to do here if the user says no?
        else:
            self.model.setCurrentTask(existingTask)

            #TODO:  allow user to either return to task entry or create new task
            #TODO:  make a separate logic flow to account for creation of new tasks

    def getValidQuantityInput(self):
        quantitySet = False
        while not(quantitySet):
            try:
                inputStr = self.view.promptQuantity(self.model.getCurrentTask().title, self.model.getCurrentDate())
                quantity = int(inputStr)
                self.model.setCurrentQuantity(quantity)
                quantitySet = True
            except ValueError:
                self.view.showInputError(inputStr)

    def checkForQuit(self, inputStr):
        if inputStr in self.quitCommands:
            exit()

