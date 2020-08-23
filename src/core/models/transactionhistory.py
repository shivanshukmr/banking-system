import datetime

class TransactionHistory:
                       # loses        # gains
    def __init__(self, useracc1 :int, useracc2 :int, amount :int, date_time :datetime.datetime):
        self.useracc1 = useracc1
        self.useracc2 = useracc2
        self.amount = amount
        self.date_time = date_time

    def get_useracc1(self):
        return self.useracc1

    def get_useracc2(self):
        return self.useracc2
    
    def get_amount(self):
        return self.amount
    
    def get_datetime(self):
        return self.date_time
