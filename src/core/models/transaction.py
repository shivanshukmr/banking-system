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

    def print(self, currentuser):
        if self.user1accno is None or self.user2accno is None:
            # withdrawal or deposit
            description = currentuser.firstname + " " + currentuser.lastname
            if self.user1accno is None:
                withdrawal = "NULL"
                deposit = self.amount
            elif self.user2accno is None:
                withdrawal = self.amount
                deposit = "NULL"

        else:
            # transfer to user2accno / from user1accno
            if self.user1accno == currentuser.accno:
                # balance decreased
                description = self.user2accno
                withdrawal = self.amount
                deposit = "NULL"
            elif self.user2accno == currentuser.accno:
                # balance increased
                description = self.user1accno
                withdrawal = "NULL"
                deposit = self.amount

        print(
            "{}     {:<32} {:<12}   {:<12}".format(
                self.time_of_transaction,
                description,
                withdrawal,
                deposit,
            )
        )
