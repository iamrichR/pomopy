import datetime

class PomoLog:
    def __init__(self, date, task, quantity):
        self.date = date
        self.task = task
        self.quantity = quantity
 
    def __str__(self):
        return ("Date:  %s // Quantity:  %d // " % (self.date.strftime('%m/%d/%Y'), self.quantity)) + str(self.task)

    #TODO:  make PomoLog and Task classes directly JSON encode-able instead of doing it like this
    def getData(self):
        return {"date": self.date.strftime("%m/%d/%y"), "task": self.task.getData(), "quantity": self.quantity}