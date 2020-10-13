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
    acc = user.accno  # acc is the account no. of the current user
    balance = int(user.balance[0])
    balance += money

    # in users table
    query = "update users set balance = %s where accno=%s" % (balance, acc)
    cursor.execute(query)

    # in transaction table
    cursor.execute(
        "insert into transactionhistory(user2accno, amount) values(%s,%s)", (acc, money)
    )
    db.commit()

    # new balance object
    cursor.execute("select balance from users where accno = %s", (acc,))
    balance = cursor.fetchone()
    user.balance = balance

    print("deposited Rs.", money, "in account-", acc)


def withdraw(user):
    "Withdraw money from current users acc."

    balance = user.balance[0]
    if balance == 0:  # check for balance
        print("You can't withdraw money")
        print("Balance: 0")
    else:
        money = int(input("amount to be withdrawn"))
        balance -= money
        db = get_DB()
        cursor = get_Cursor()
        acc = user.accno  # acc is the account no. of the current user

        # in  users table
        query = "update users set balance = %s where accno=%s" % (balance, acc)
        cursor.execute(query)

        # in transaction table
        cursor.execute(
            "insert into transactionhistory(user1accno, amount) values(%s,%s)",
            (acc, money),
        )
        db.commit()

        # new balance object
        cursor.execute("select balance from users where accno = %s", (acc,))
        balance = cursor.fetchone()
        user.balance = balance

        print("withdrew Rs.", money, "from account-", acc)


def transfer(user):
    "Transfer money to other users"

    balance = user.balance[0]
    if balance == 0:  # check for balance
        print("You can't transfer money")
        print("Balance: 0")
    else:
        db = get_DB()
        cursor = get_Cursor()
        acc2 = int(input("account number of the recipient"))
        money = int(input("amount to be trasfered"))
        acc = user.accno

        # in users table
        query = "update users set balance = balance - %s where accno=%s" % (money, acc)
        cursor.execute(query)
        query2 = "update users set balance = balance + %s where accno=%s" % (
            money,
            acc2,
        )
        cursor.execute(query2)
        db.commit

        # in transaction  table
        cursor.execute(
            "insert into transactionhistory(user1accno, user2accno, amount) values(%s,%s,%s)",
            (acc, acc2, money),
        )
        db.commit()

        # new balance object
        cursor.execute("select balance from users where accno = %s", (acc,))
        balance = cursor.fetchone()
        user.balance = balance

        print("transfered Rs.", money, "to account no.-", acc2)
