import json

class FileManager:

    def __init__(self):
        a = 1

    
    def updateFile(self, path, data):
        with open(path, 'w') as writeFile:
            writeFile.write(data)

    #for simplicity's purposes, methods in this class that
    #refer to "JSONList" assume the given JSON file consists of a
    #single item, a list, containing the relevant data
    def updateJSONList(self, path, newItem):
        listName, oldData = self.fetchJSONList(path)
        newData = []
        if oldData is not None:
            newData += oldData
        newData.append(newItem)
        self.updateFile(path, json.dumps({listName:newData}))

    def fetchJSONList(self, path):
        fileData = self.getJSONDataFromFile(path)
        if(isinstance(fileData, dict) and len(fileData) > 0):
            first_item = list(fileData.values())[0]
            first_key = list(fileData.keys())[0]
            if(isinstance(first_item, list)):
                return (first_key, first_item)
        return None

    def getJSONDataFromFile(self, path):
        with open(path, 'r') as dataSource:
            data = dataSource.read()
        try:
            jsonData = json.loads(data)
            return jsonData
        except ValueError:
            return None


if __name__ == "__main__":
    #TODO: make this a test whenever you add tests
    file1 = "./emptyFile.json"
    file2 = "./test.json"
    fm = FileManager()

    for n in range(5,100):
        fm.updateJSONList(file2, n)