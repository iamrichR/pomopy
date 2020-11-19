class Task:
    def __init__(self, title, tags):
        self.title = title
        self.tags = tags
    
    def addTag(self, tag):
        self.tags.append(tag)
    
    def __str__(self):
        #return "title:  " + str(self.title) + " | tags:  " + str(self.tags)
        return ("Title:  %s | Tags:  %s" % (str(self.title), str(self.tags)))

    def getData(self):
        return {"title": self.title, "tags": self.tags}



#  TODO:  add a comparison method so that you can make a complete list of existing Tasks across all archives