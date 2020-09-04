from AppView import AppView
from AppModel import AppModel

class AppController:
    def __init__(self):
        self.view = AppView()
        self.model = AppModel()

    def start(self):
        self.dailyLog()

    def dailyLog(self):
        quit = False
        while not quit:
            dateStr = self.view.promptDate(self.model.getPrefDateFmt())
            print(self.model.isDateValid(dateStr))

