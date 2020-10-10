# get connection object and cursor object from dbconnector.connector
# deposit and withdraw money
# transfer money to other users

from core.db.connector import *


def deposit(user):
    "Deposit money to current users acc."

    money = int(input("amount to be deposited"))

    # in users table
    acc = user.accno  # acc is the account no. of the current user

    query = "update users set balance = balance + %s where accno=%s" % (money, acc)
    cursor.execute(query)
    db.commit

    # in transaction table

    print("deposited Rs.", money, "in account-", acc)


def withdraw(user):
    "Withdraw money from current users acc."
    get_DB()
    cursor = get_Cursor()
    money = int(input("amount to be withdrawn"))

    # in users table
    acc = user.accno  # acc is the account no. of the current user

    query = "update users set balance = balance - %s where accno=%s" % (money, acc)
    cursor.execute(query)
    db.commit

    # in transaction table

    print("withdrew Rs.", money, "from account-", acc)


def transfer(user):
    "Transfer money to other users"
    get_DB()
    cursor = get_Cursor()
    acc2 = int(input("account number of the recipient"))
    money = int(input("amount to be trasfered"))
    acc = user.accno

    # in users table
    query = "update users set balance = balance - %s where accno=%s" % (money, acc)
    cursor.execute(query)
    query2 = "update users set balance = balance + %s where accno=%s" % (money, acc2)
    cursor.execute(query2)
    db.commit

    # in transaction  table

    print("transfered Rs.", money, "to account no.-", acc2)
