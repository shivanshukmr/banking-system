class User:
    def __init__(self, accno, username, balance):
        self.accno = accno
        self.username = username
        self.balance = balance

    def get_accno(self):
        return self.accno

    def get_username(self):
        return self.username
    
    def get_balance(self):
        return self.balance
