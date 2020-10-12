# get connection object and cursor object from dbconnector.connector
# deposit and withdraw money
# transfer money to other users
from core.db.connector import get_Cursor, get_DB
from core.models.user import User


def deposit(user):
    "Deposit money to current users acc."
    db = get_DB()
    cursor = get_Cursor()
    money = int(input("amount to be deposited"))

    # in users table
    acc = user.accno  # acc is the account no. of the current user
    balance = int(user.balance[0])
    balance += money

    query = "update users set balance = %s where accno=%s" % (balance, acc)
    cursor.execute(query)
    db.commit

    # in transaction table
    cursor.execute(
        "insert into transactionhistory(user2accno, amount) values(%s,%s)", (acc, money)
    )
    db.commit()

    print("deposited Rs.", money, "in account-", acc)


def withdraw(user):
    "Withdraw money from current users acc."
    db = get_DB()
    cursor = get_Cursor()
    money = int(input("amount to be withdrawn"))

    # in users table
    acc = user.accno  # acc is the account no. of the current user
    balance = int(user.balance[0])
    balance -= money

    query = "update users set balance = %s where accno=%s" % (balance, acc)
    cursor.execute(query)
    db.commit

    # in transaction table
    cursor.execute(
        "insert into transactionhistory(user1accno, amount) values(%s,%s)", (acc, money)
    )
    db.commit()

    print("withdrew Rs.", money, "from account-", acc)


def transfer(user):
    "Transfer money to other users"
    db = get_DB()
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
    cursor.execute(
        "insert into transactionhistory(user1accno, user2accno, amount) values(%s,%s,%s)",
        (acc, acc2, money),
    )
    db.commit()

    print("transfered Rs.", money, "to account no.-", acc2)
