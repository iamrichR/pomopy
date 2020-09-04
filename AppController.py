from AppView import AppView

class AppController:
    def __init__(self):
        self.view = AppView()

    def start(self):
        res = self.view.sayHi()
        print("You said " + res)
