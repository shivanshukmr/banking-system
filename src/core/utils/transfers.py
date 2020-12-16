from core.db.connector import get_Cursor, get_DB


def deposit(user):
    """
    Deposit money to current users acc.
    """

    db = get_DB()
    cursor = get_Cursor()
    money = int(input("Amount to be deposited:"))
    acc = user.accno  # acc is the account no. of the current user
    balance = int(user.balance)
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

    print("Deposited Rs.", money, "in account-", acc)


def withdraw(user):
    """
    Withdraw money from current users acc.
    """

    balance = user.balance
    if balance == 0:  # check for balance
        print("You can't withdraw money.")
        print("Balance: 0")
    else:
        money = int(input("Amount to be withdrawn:"))
        if money > balance:
            print("Amount exceeds current balance.")
            print("Can't withdraw.")
        else:
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

            print("Withdrew Rs.", money, "from account-", acc)


def transfer(user):
    """
    Transfer money to other users
    """

    balance = user.balance
    if balance == 0:  # check for balance
        print("You can't transfer money.")
        print("Balance: 0")
    else:
        db = get_DB()
        cursor = get_Cursor()
        acc = user.accno
        acc2 = int(input("Account number of the recipient:"))
        cursor.execute("select * from users")  # cursor = get_Cursor()
        data = cursor.fetchall()
        a = False
        for row in data:
            if row[2] == acc2 and acc2 != acc:
                a = True
                money = int(input("Amount to be trasfered:"))
                if money > balance:
                    print("Amount exceeds current balance.")
                    print("Can't transfer.")
                else:
                    # in users table
                    query = "update users set balance = balance - %s where accno=%s" % (
                        money,
                        acc,
                    )
                    cursor.execute(query)
                    query2 = (
                        "update users set balance = balance + %s where accno=%s"
                        % (
                            money,
                            acc2,
                        )
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

                    print("Transfered Rs.", money, "to account no.-", acc2)
        if a == False:
            print("Account no.", acc2, "doesn't exist.")
