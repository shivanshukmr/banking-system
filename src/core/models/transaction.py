from core.db.connector import get_DB


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
            description = "Self"
            if self.user1accno is None:
                withdrawal = "NULL"
                deposit = self.amount
            elif self.user2accno is None:
                withdrawal = self.amount
                deposit = "NULL"

        else:
            # transfer to user2accno / from user1accno
            db = get_DB()
            cursor = db.cursor()
            if self.user1accno == currentuser.accno:
                # balance decreased
                cursor.execute(
                    "SELECT firstname, lastname FROM users WHERE accno = {}".format(
                        self.user2accno
                    )
                )
                output = cursor.fetchone()
                description = output[0] + " " + output[1]
                withdrawal = self.amount
                deposit = "NULL"
            elif self.user2accno == currentuser.accno:
                # balance increased
                cursor.execute(
                    "SELECT firstname, lastname FROM users WHERE accno = {}".format(
                        self.user1accno
                    )
                )
                output = cursor.fetchone()
                description = output[0] + " " + output[1]
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
