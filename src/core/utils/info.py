from core.db.connector import get_Cursor
from core.tables.transaction import Transaction


def get_users(user):
    """
    Return other users w/ bankaccount nos.
    """
    cursor = get_Cursor()

    # acc is the account no. of the current user
    acc = user.accno
    query = "select accno, firstname, lastname from users where accno <> %s" % (acc,)
    cursor.execute(query)
    return cursor.fetchall()


def get_balance(user):
    """
    Return balance of current user
    """
    return user.balance


def get_transactionhistory(user):
    """
    Return transaction history of current user
    """
    cursor = get_Cursor()
    cursor.execute(
        "SELECT * FROM transactionhistory WHERE user1accno = {0} OR user2accno = {0} ORDER BY time_of_transaction DESC".format(
            user.accno,
        )
    )
    transaction_hist = []
    for transaction in cursor.fetchall():
        transaction_hist.append(Transaction.fromTuple(transaction))

    return transaction_hist
