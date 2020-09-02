class User:
    def __init__(self, firstname, lastname, accno, datecreated, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.accno = accno
        self.datecreated = datecreated
        self.balance = balance

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_accno(self):
        return self.accno

    def get_datecreated(self):
        return self.datecreated

    def get_balance(self):
        return self.balance
