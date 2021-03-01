class Logger:
    def __init__(self):
        self.listSaveString = []

    def Log(self,stringLog):
        if stringLog != "" and stringLog != " ":
            self.listSaveString.append(stringLog)
            
    def GetLog(self):
        return self.listSaveString
