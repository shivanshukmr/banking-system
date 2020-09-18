# get connection object and cursor object from dbconnector.connector
# display other users w/ bankaccout nos.
# display your account info
# display balance
# display transaction history(current user)

def getusers():
    "display other users w/ bankaccout nos."
    from db.connector import *
    get_DB()
    cursor = get_Cursor()

    # acc is the account no. of the current user
    query = "select accno, firstname, lastname from users where accno <> %s" % (
        acc,)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def details():
    "shows firstname, lastname accno. and balance"
    from db.connector import *
    get_DB()
    cursor = get_Cursor()

    # acc is the account no. of the current user
    query = "select accno, firstname, lastname, balance, date_created from users where accno = %s" % (
        acc,)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def balance():
    "balance of current user"
    from db.connector import *
    get_DB()
    cursor = get_Cursor()

    # acc is the account no. of the current user
    query = "select balance from users where accno=%s" % (acc,)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def trans_history():
    "display transaction history of current user"
    from db.connector import *
    get_DB()
    cursor = get_Cursor()
