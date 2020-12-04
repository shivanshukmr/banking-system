# get connection object and cursor object from dbconnector.connector
# display other users w/ bankaccout nos.
# display your account info
# display balance
# display transaction history(current user)
from core.db.connector import get_Cursor
from core.tables.transaction import Transaction
from gui.Assets.assets import colour
from tkinter import Label, Button


def getusers(user):
    "display other users w/ bankaccout nos."
    cursor = get_Cursor()

    # acc is the account no. of the current user
    acc = user.accno
    query = "select accno, firstname, lastname from users where accno <> %s" % (acc,)
    cursor.execute(query)
    # users table
    print("{:<12} {:<15} {:<15}".format("Account no.", "Firstname", "Lastname"))
    for row in cursor.fetchall():
        print(
            "{:<12} {:<15} {:<15}".format(
                row[0],
                row[1],
                row[2],
            )
        )


def details(self, user):
    # "shows firstname, lastname accno. and balance"
    date = str(user.datecreated[0])
    acc_l = Label(self, text="Account no.:" + user.accno[0], bg=colour, fg=font_c)
    fist_l = Label(self, text="Firstname:" + user.firstname[0], bg=colour, fg=font_c)
    last_l = Label(self, text="Lastname:" + user.lastname[0], bg=colour, fg=font_c)
    bal_l = Label(self, text="Balance:" + user.balance[0], bg=colour, fg=font_c)
    date_l = Label(self, text="Account created on:" + date, bg=colour, fg=font_c)

    acc_l.pack()
    fist_l.pack()
    last_l.pack()
    bal_l.pack()
    date_l.pack()


def details_button(self, user):
    detail_b = Button(self, text="Account Details", command=lambda: details(self, user))


def balance(self, user):
    bal_l = Label(self, text="Balance:" + user.balance[0], bg=colour, fg=font_c)
    bal_l.pack()


def balance_button(self, user):
    bal_b = Button(self, text="Balance", command=lambda: balance(self, user))


def transactionHistory(user):
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
