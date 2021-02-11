# get connection object and cursor object from dbconnector.connector
# user creation
# user authentication/signin
from core.db.connector import get_Cursor, get_DB
from core.tables.user import User

# =================registration=================================================================
def usercreation():
    """
    Gets name, password(twice), and updates db.
    user gets auto-generated accno.
    """
    import getpass

    cursor = get_Cursor()
    db = get_DB()
    print()
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
    print("")
    print("Created new account.")
    cursor.execute("select max(accno) from users;")
    acc = cursor.fetchone()
    print("Your account number is-", acc[0])
    print()


# ===================login=======================================================================
def userauthentication():
    import getpass

    cursor = get_Cursor()

    """
    Gets account no., password and check in db
    returns user object
    """
    print()
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
        print()
        return User(acc, firstname, lastname, datecreated, balance)

    if flag == False:
        print()
        return None


# ============================change detaails====================================================
def updateinfo(user):
    import getpass

    print()
    db = get_DB()
    acc = user.accno
    cursor = get_Cursor()
    flag = True
    while flag == True:
        print("firstname  |  lastname  |  password")
        print()
        q = input("What would you like to change from above?")
        if q == "firstname":
            fname = input("Your firstname:")
            query = "update users set firstname = %s where accno=%s"
            val = (fname, acc)
            cursor.execute(query, val)
            db.commit()
            print("firstname would be updated after you signout")

        elif q == "lastname":
            lname = input("Your lastname:")
            query = "update users set lastname = %s where accno=%s"
            val = (lname, acc)
            cursor.execute(query, val)
            db.commit()
            print("lastname would be updated after you signout.")

        elif q == "password":
            query = "select * from users where accno=%s" % (acc)
            cursor.execute(query)
            data = cursor.fetchall()
            cur_pass = getpass.getpass("Enter your current password:")
            for row in data:
                # checks every record from column 3(accno) with the users input
                if row[3] == cur_pass:
                    flag = True
                    while flag:  # taking password twice and cnfirming password
                        passwd = getpass.getpass("Enter new password:")
                        passwd2 = getpass.getpass("Confirm new password:")
                        if passwd == passwd2:
                            print("Password confirmed.")
                            flag = False
                        else:
                            print("Passwords do not match.")
                            print("Try again.")
                            flag = True
                    break
            if flag == False:
                query = "update users set passwd = %s where accno=%s" % (
                    passwd,
                    acc,
                )
                cursor.execute(query)
                db.commit()
                print("Password updated")
        else:
            print("You didnt choose the correct option")
        print()
        question = input("Would you like to change anything else?(yes/no)")
        if question == "no":
            flag = False
    print()


# =======================delete account==========================================================
def delete(user):
    import getpass

    db = get_DB()
    acc = user.accno

    cursor = get_Cursor()
    query = "select * from users where accno=%s" % (acc)
    cursor.execute(query)
    data = cursor.fetchall()
    print()
    print("you're account will be permanently closed")
    confirm = input("Are you sure you want to continue?(yes/no)")
    if confirm == "yes":
        flag = False
        while flag == False:  # user authentication
            print()
            acc = int(input("Enter your account no.:"))
            if acc == 0:
                break
            passwd = getpass.getpass("Enter your password:")

            for row in data:
                # checks every record from column 3(accno) with the users input
                if row[2] == acc and row[3] == passwd:
                    print()
                    print("Account no. and password confirmed.")
                    flag = True
                    break
            if flag == False:
                print()
                print("Account no. or the password is wrong. Try again.")
                print("Press 0 to cancel")

        if flag == True:
            print()
            confirm2 = input(
                "The account will now be closed. Press 'enter' to continue or 'c' to cancel."
            )
            if confirm2 == "c":
                print("Canceled account deletion.")
            else:
                money = user.balance[0]
                if money != 0:
                    print()
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
                            break
                    if a == False:
                        print("Account no.", acc2, "doesn't exist.")
                else:
                    print("Balance: 0")
                val = ("admin", acc)
                query = "update users set passwd = %s where accno=%s"
                cursor.execute(query, val)
                db.commit()
                print()
                print("Account has been closed.")
                print("You are signed out.")
                print()
                return None
