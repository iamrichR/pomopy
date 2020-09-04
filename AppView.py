class AppView:
    # def __init__(self):
    #     self.x = 1

    def promptDate(self, prefDateFmt):
        dateStr = input("Please enter the date to be logged\nin %s format\n" % prefDateFmt)
        return dateStr