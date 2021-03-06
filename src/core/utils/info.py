from core.db.connector import get_Cursor
from core.tables.transaction import Transaction


def getusers(user):
    "display other users w/ bankaccout nos."
    cursor = get_Cursor()
    print()
    # acc is the account no. of the current user
    acc = user.accno
    query = (
        "select accno, firstname, lastname from users where accno <> %s and passwd <> 'administrator123'"
        % (acc)
    )
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
    print()


def details(user):
    # "shows firstname, lastname accno. and balance"
    print()
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
    print()


def balance(user):
    # "balance of current user"
    print("")
    print("Your balance:", user.balance[0])
    print("")


def transaction_history(user):
    """
    Display transaction history of current user
    """
    print("")

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
        print()
    else:
        # print transactions
        print(
            "{:<23} {:<32} {:<12}   {:<12}".format(
                "Date", "Description", "Withdrawal", "Deposit"
            )
        )
        for transaction in transaction_hist:
            transaction.print(user)
    print()
