# get connection object and cursor object from dbconnector.connector
# deposit and withdraw money
# transfer money to other users

from core.db.connector import *


def deposit(user):
    "Deposit money to current users acc."
    get_DB()
    cursor = get_Cursor()
    money = int(input("money to be deposited"))

    # in users table
    acc = user.accno  # acc is the account no. of the current user

    query = "update users set balance += %s where accno=%s" % (money, acc)
    cursor.execute(query)
    db.commit

    # in transaction table

    print("deposited", money, "in account-", acc)


def withdraw(user):
    "Withdraw money from current users acc."
    money = int(input("money to be withdrawn"))

    # in users table
    acc = user.accno  # acc is the account no. of the current user

    query = "update users set balance -= %s where accno=%s" % (money, acc)
    cursor.execute(query)
    db.commit

    # in transaction table

    print("withdrew", money, "from account-", acc)


def transfer():
    "Transfer money to other users"
