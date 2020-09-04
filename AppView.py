class AppView:
    def __init__(self):
        self.x = 1

    def sayHi(self):
        print("hello")

    def promptDate(self):
        #TODO:  have the Controller (via the model) pass in the expected format instead of hard-coding here
        dateStr = input("Please enter the date to be logged\nmm/dd/yy format\n")
        return dateStr