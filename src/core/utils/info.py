# get connection object and cursor object from dbconnector.connector
# display other users w/ bankaccout nos.
# display your account info
# display balance
# display transaction history(current user)
from core.db.connector import get_Cursor
from core.models.transaction import Transaction


def getusers(user):
    "display other users w/ bankaccout nos."
    cursor = get_Cursor()

    # acc is the account no. of the current user
    acc = user.accno
    query = "select accno, firstname, lastname from users where accno <> %s" % (acc,)
    cursor.execute(query)
    # users table
    users = cursor.fetchall()
    if users == []:
        print("No users")
    else:
        print("{:<12} {:<15} {:<15}".format("Account no.", "Firstname", "Lastname"))
        for row in users:
            print(
                "{:<12} {:<15} {:<15}".format(
                    row[0],
                    row[1],
                    row[2],
                )
            )


def details(user):
    # "shows firstname, lastname accno. and balance"

    # acc is the account no. of the current user
    # query = (
    #    "select accno, firstname, lastname, balance, date_created from users where accno = %s"
    #    % (acc,)
    # )
    # cursor.execute(query)
    # for row in cursor.fetchall():
    #    print(row)
    date = str(user.datecreated[0])
    print(
        "{:<12} {:<15} {:<15} {:<12} {:<20}".format(
            "Account no.", "Firstname", "Lastname", "Balance", "Account created on"
        )
    )
    print(
        "{:<12} {:<15} {:<15} {:<12} {:<20}".format(
            user.accno,
            user.firstname[0],
            user.lastname[0],
            user.balance[0],
            date,
        )
    )


def balance(user):
    # "balance of current user"
    # from db.connector import *
    # get_DB()
    # cursor = get_Cursor()

    # # acc is the account no. of the current user
    # query = "select balance from users where accno=%s" % (acc,)
    # cursor.execute(query)
    # for row in cursor.fetchone():
    #     print(row)
    print("Your balance:", user.balance[0])


def transactionHistory(user):
    """
    Display transaction history of current user
    """
    # get all transactions involving current user (recent to oldest)
    cursor = get_Cursor()
    cursor.execute(
        "SELECT * FROM transactionhistory WHERE user1accno = {0} OR user2accno = {0} ORDER BY time_of_transaction DESC".format(
            user.accno,
        )
    )
    transaction_hist = []
    for transaction in cursor.fetchall():
        transaction_hist.append(Transaction.fromTuple(transaction))

    if transaction_hist == []:
        print("No Transactions")
    else:
        # print transactions
        print(
            "{:<23} {:<32} {:<12}   {:<12}".format(
                "Date", "Description", "Withdrawal", "Deposit"
            )
        )
        for transaction in transaction_hist:
            transaction.print(user)
