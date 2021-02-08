# get connection object and cursor object from dbconnector.connector
# user creation
# user authentication/signin
from core.db.connector import get_Cursor, get_DB
from core.models.user import User


def usercreation():
    """
    Gets name, password(twice), and updates db.
    user gets auto-generated accno.
    """
    import getpass

    cursor = get_Cursor()
    db = get_DB()

    fname = input("Your firstname:")
    lname = input("Your lastname:")

    flag = True
    while flag:  # taking password twice and cnfirming password
        for i in range(0, 2):
            if i == 0:
                passwd = getpass.getpass("Enter a password:")
                a = passwd
            if i == 1:
                passwd = getpass.getpass("Confirm password:")
                if passwd == a:
                    print("Password confirmed.")
                    flag = False
                else:
                    print("Passwords do not match.")
                    print("Try again.")
                    flag = True

    cursor.execute(
        "insert into users(firstname,lastname,passwd) values(%s,%s,%s)",
        (fname, lname, passwd),
    )  # cursor=get_Cursor()
    db.commit()
    print("Created new account.")
    cursor.execute("select max(accno) from users;")
    acc = cursor.fetchone()
    print("Your account number is-", acc[0])


def userauthentication():
    import getpass

    cursor = get_Cursor()

    """
    Gets account no., password and check in db
    returns user object
    """

    flag = False
    cursor.execute("select * from users")  # cursor = get_Cursor()
    data = cursor.fetchall()

    while flag == False:  # user authentication
        acc = int(input("Enter your account no.:"))
        if acc == 0:
            break
        passwd = getpass.getpass("Enter your password:")

        for row in data:
            # checks every record from column 3(accno) with the users input
            if row[2] == acc and row[3] == passwd:
                flag = True
                break
        if flag == False:
            print("Account no. or the password is wrong. Try again.")
            print("Press 0 to skip signin")

    # returns true if user verified else false

    if flag == True:
        # get firstname, lastname, datecreated, and balance
        cursor.execute("select firstname from users where accno = %s", (acc,))
        firstname = cursor.fetchone()
        cursor.execute("select lastname from users where accno = %s", (acc,))
        lastname = cursor.fetchone()
        cursor.execute("select date_created from users where accno = %s", (acc,))
        datecreated = cursor.fetchone()
        cursor.execute("select balance from users where accno = %s", (acc,))
        balance = cursor.fetchone()
        # return User object
        print("You are signed in.")
        return User(acc, firstname, lastname, datecreated, balance)

    if flag == False:
        return None


def updateinfo(user):
    db = get_DB()
    acc = user.accno


def delete(user):
    import getpass

    db = get_DB()
    acc = user.accno

    cursor = get_Cursor()
    query = "select * from users where accno=%s" % (acc)
    cursor.execute(query)
    data = cursor.fetchall()

    print("you're account will be permanently closed")
    confirm = input("Are you sure you want to continue?(yes/no)")
    if confirm == "yes":
        flag = False
        while flag == False:  # user authentication
            acc = int(input("Enter your account no.:"))
            if acc == 0:
                break
            passwd = getpass.getpass("Enter your password:")

            for row in data:
                # checks every record from column 3(accno) with the users input
                if row[2] == acc and row[3] == passwd:
                    print("Account no. and password confirmed.")
                    flag = True
                    break
            if flag == False:
                print("Account no. or the password is wrong. Try again.")
                print("Press 0 to cancel")

        if flag == True:
            confirm2 = input(
                "The account will now be closed. Press 'enter' to continue or 'c' to cancel."
            )
            if confirm2 == "c":
                print("Canceled account deletion.")
            else:
                money = user.balance[0]
                if money != 0:
                    acc2 = int(
                        input(
                            "To which account no. would you like to transfer your money"
                        )
                    )
                    cursor.execute("select * from users")  # cursor = get_Cursor()
                    data = cursor.fetchall()
                    a = False
                    for row in data:
                        if row[2] == acc2 and acc2 != acc:
                            a = True
                            # in users table
                            query = (
                                "update users set balance = balance - %s where accno=%s"
                                % (
                                    money,
                                    acc,
                                )
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
                            print("Transfered Rs.", money, "to account no.-", acc2)
                        if a == False:
                            print("Account no.", acc2, "doesn't exist.")
                        if a == True:
                            break
                passwd = "admin"
                query2 = "update users set passwd = %s where accno=%s" % (
                    money,
                    acc,
                )
                db.commit
                print("Account has been closed.")
                print("You are signed out.")
                return None
