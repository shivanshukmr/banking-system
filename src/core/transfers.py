# get connection object and cursor object from dbconnector.connector
# deposit and withdraw money
# transfer money to other users

def deposite():
    "Deposit money to current users acc."
    money = int(input("money to be deposited"))
    from connector import *
    get_DB()
    cursor = get_Cursor()

    # in users table
    query = "update users set balance += money"


def withdraw():
    "Withdraw money from current users acc."


def transfer():
    "Transfer money to other users"


deposite()
