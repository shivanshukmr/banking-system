class User:
    def __init__(self, accno, username, balance):
        self.accno = accno
        self.username = username
        self.balance = balance

    def getusername(self):
        return self.username
    
    def getaccno(self):
        return self.accno
    
    def getbalance(self):
        return self.balance
