import json
import os

class FileManager:

    # def __init__(self):
    #     a = 1

    
    def __updateFile(self, path, data):
        with open(path, 'w') as writeFile:
            writeFile.write(data)

    #for simplicity's purposes, methods in this class that
    #refer to "JSONList" assume the given JSON file consists of a
    #single item, a list, containing the relevant data
    def addItemtoList(self, path, newItem, providedListName=None):
        listName, oldData = self.fetchJSONList(path)
        if(providedListName is not None):
            listName = providedListName
        newData = []
        if oldData is not None:
            newData += oldData
        newData.append(newItem)
        self.__updateFile(path, json.dumps({listName:newData}))

    def updateList(self, path, newList):
        listName, oldData = self.fetchJSONList(path)
        self.__updateFile(path, json.dumps({listName:newList}))

    def fetchJSONList(self, path):
        fileData = self.__getJSONDataFromFile(path)
        if(isinstance(fileData, dict) and len(fileData) > 0):
            first_item = list(fileData.values())[0]
            first_key = list(fileData.keys())[0]
            if(isinstance(first_item, list)):
                return (first_key, first_item)
        return (None, None)

    def __getJSONDataFromFile(self, path):
        try:
            with open(path, 'r') as dataSource:
                data = dataSource.read()
            try:
                jsonData = json.loads(data)
                return jsonData
            except ValueError:
                return None
        except FileNotFoundError:
            return None


if __name__ == "__main__":
    try:
        #TODO: make this a test whenever you add tests
        fm = FileManager()
        filename1 = "./emptyFile.json"
        filename2 = "./test.json"
        for filename in (filename1, filename2):
            if os.path.exists(filename):
                os.remove(filename)
        file1 = open(filename1, "w")
        file1.close()
        file2 = open(filename2,"w")
        file2.write(json.dumps(fm))
        file2.write(json.dumps({"testData":[1,2,3,4]}))
        file2.close()
        for n in range(5,100):
            fm.addItemtoList(file2.name, n)
        if(len(fm.fetchJSONList(filename2)) == 99):
            print("test ran successfully")
        else:
            print("test failed, %s data written incorrectly" % (filename2))
    except Exception as e:
        print("test failed, error occurred.")
        print("<" + str(e) + ">")