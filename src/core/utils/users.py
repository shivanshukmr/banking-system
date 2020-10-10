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

    cursor = get_Cursor()
    db = get_DB()

    name = input("your firstname:")
    lname = input("your lastname:")

    flag = True  # taking password twice

    while flag:
        for i in range(0, 2):
            if i == 0:
                passwd = input("enter a password")
                a = passwd
            if i == 1:
                passwd = input("confirm password")
                if passwd == a:
                    print("password confirmed")
                    flag = False
                else:
                    print("password do not match")
                    flag = True

    query = "insert into users(name, lastname, passwd) values(%s,%s,%s)" % (
        name,
        lname,
        passwd,
    )
    cursor.execute(query)  # cursor=get_Cursor()
    db.commit()
    print("created new account")


def userauthentication():

    cursor = get_Cursor()
    db = get_DB()

    """
    Gets account no., password and check in db
    returns user object
    """

    flag = False
    cursor.execute("select * from users")  # cursor = get_Cursor()
    data = cursor.fetchall()

    while flag:  # user authentication
        acc = int(input("enter your accno"))
        passwd = input("enter your password")

        for row in data:
            # checks every record from column 3(accno) with the users input
            if row[2] == acc and row[3] == passwd:
                flag = True
                break
            else:
                print("account no. or the password is wrong")
                break
    # returns true if user verified else false
    if flag == True:
        # get firstname, lastname, datecreated, and balance
        cursor.execute("select name from users where accno = %s" % (acc,))
        firstname = cursor.fetchone()
        cursor.execute("select lastname from users where accno = %s" % (acc,))
        lastname = cursor.fetchone()
        cursor.execute(
            "select datecreated from users where accno = %s" % (acc,))
        datecreated = cursor.fetchone()
        cursor.execute("select balance from users where accno = %s" % (acc,))
        balance = cursor.fetchone()
        # return User object

        return User(user, acc, firstname, lastname, datecreated, balance)

    if flag == False:
        return None
