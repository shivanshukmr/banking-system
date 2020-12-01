class Transaction:
    def __init__(self, user1accno, user2accno, amount, time_of_transaction):
        self.user1accno = user1accno
        self.user2accno = user2accno
        self.amount = amount
        self.time_of_transaction = time_of_transaction

    # get a transaction object from tuple
    @staticmethod
    def fromTuple(transaction_tuple):
        return Transaction(
            transaction_tuple[0],
            transaction_tuple[1],
            transaction_tuple[2],
            transaction_tuple[3],
        )
