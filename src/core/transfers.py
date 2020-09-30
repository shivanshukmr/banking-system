# get connection object and cursor object from dbconnector.connector
# deposit and withdraw money
# transfer money to other users

from db.connector import *


def deposite():
    "Deposit money to current users acc."
    get_DB()
    cursor = get_Cursor()
    money = int(input("money to be deposited"))

    # in users table
    # acc is the account no. of the current user
    query = "update users set balance += %s where accno=%s" % (money, acc)
    cursor.execute(query)
    db.commit

    # in transaction table


def withdraw():
    "Withdraw money from current users acc."
    "Deposit money to current users acc."
    money = int(input("money to be withdrawn"))

    # in users table
    # acc is the account no. of the current user

    query = "update users set balance -= %s where accno=%s" % (money, acc)
    cursor.execute(query)
    db.commit

    # in transaction table


def transfer():
    "Transfer money to other users"
