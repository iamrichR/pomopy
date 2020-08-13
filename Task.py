class Task:
    def __init__(self, title, tags):
        self.title = title
        self.tags = tags
    
    
    def __str__(self):
        #return "title:  " + str(self.title) + " | tags:  " + str(self.tags)
        return ("Title:  %s | Tags:  %s" % (str(self.title), str(self.tags)))



#  TODO:  add a comparison method so that you can make a complete list of existing Tasks across all archives