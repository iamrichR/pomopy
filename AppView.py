class AppView:
    # def __init__(self):
    #     self.x = 1

    def promptDate(self, prefDateFmt):
        dateStr = input("\nPlease enter the date to be logged\nin %s format\n" % prefDateFmt).upper()
        return dateStr

    def promptTask(self):
        print("\nWhat task are you logging?")
        print("Enter 'TASK_LIST' to see list of existing task names.")
        return input().upper()

    def promptQuantity(self, taskTitle, dateStr):
        print("\nHow many Pomodoros of %s logged on %s" % (taskTitle, dateStr))
        print("Please enter a positive whole number")
        return input()

    def showInputError(self, inputStr):
        print("\nINPUT ERROR:  " + inputStr)

    def errTaskNotFound(self):
        print("That task was not found in the database")

    def promptNewTask(self, taskStr):
        print("Would you like to save %s as a new task?" % taskStr)
        return input().upper()

    def promptTaskTags(self, taskStr):
        print("\nPlease enter a tag to apply to the %s task" % taskStr)
        #TODO:  better way to phrase this
        print("When finished, type nothing and press enter.")
        return input().upper()

    def errTagNeeded(self):
        print("\nERROR:  A task must have at least one tag.")

    def promptDailyLogContinue(self, dateStr):
        print("\nWould you like to continue logging tasks for %s" % dateStr)
        inputStr = input().upper()
        return inputStr

    