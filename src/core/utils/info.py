from core.db.connector import get_Cursor
from core.tables.transaction import Transaction


def get_users(accno):
    """
    Return other users w/ bankaccount nos.
    """
    cursor = get_Cursor()

    # acc is the account no. of the current user
    query = "select accno, firstname, lastname from users where accno <> %s" % (accno,)
    cursor.execute(query)
    return cursor.fetchall()


def get_transactionhistory(accno):
    """
    Return transaction history of given acc no.
    """
    cursor = get_Cursor()
    cursor.execute(
        "SELECT * FROM transactionhistory WHERE user1accno = {0} OR user2accno = {0} ORDER BY time_of_transaction DESC".format(
            accno,
        )
    )
    transaction_hist = []
    for transaction in cursor.fetchall():
        transaction_hist.append(Transaction.fromTuple(transaction))

    return transaction_hist
