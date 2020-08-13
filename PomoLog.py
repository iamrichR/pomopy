import datetime

class PomoLog:
    def __init__(self, date, quantity, task):
        self.date = date
        self.quantity = quantity
        self.task = task
 
    def __str__(self):
        return ("Date:  %s // Quantity:  %d // " % (self.date.strftime('%m/%d/%Y'), self.quantity)) + str(self.task)