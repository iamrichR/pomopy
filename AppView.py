class AppView:
    # def __init__(self):
    #     self.x = 1

    def promptDate(self, prefDateFmt):
        dateStr = input("\nPlease enter the date to be logged\nin %s format\n" % prefDateFmt)
        return dateStr

    def showInputError(self, inputStr):
        print("\nINPUT ERROR:  " + inputStr)

    def promptTask(self):
        print("\nWhat task are you logging?")
        #TODO:  Implement the "task list" thing here
        print("Enter 'TASK_LIST' to see list of existing task names.")
        return input()

    def errTaskNotFound(self):
        print("That task was not found in the database")