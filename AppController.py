from AppView import AppView

class AppController:
    def __init__(self):
        self.view = AppView()

    def start(self):
        self.dailyLog()

    def dailyLog(self):
        quit = False
        while not quit:
            dateStr = self.view.promptDate()
            print("you entered " + dateStr + "\n")
            #TODO:  here's where the model would convert and validate the dateStr
