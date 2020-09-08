# get connection object and cursor object from dbconnector.connector
# user creation
# user authentication/signin

# to create table

# from core.db import connector
# get_DB()
#cursor = get_Cursor()
# query = '''create table users
#    (name varchar(100) NOT NULL,
#    lastname varchar(100) NOT NULL,
#    accno int(6) PRIMARY KEY AUTO_INCREMENT, let first accno be setted by us as 123456
#    passwd int(6) NOT NULL,
#    date_created datetime NOt NULL,
#    balance int);
#    '''
# cursor.execute(query)


def usercreation():
    '''
    Gets name, password(twice), and updates db.
    user gets auto-generated accno.
    '''
    name = input("your firstname:")
    lname = input("your lastname:")

    flag = True  # taking password twice
    while flag:
        for i in range(0, 2):
            if i == 1:
                print('confirm password')
            passwd = int(
                input("enter your password(only 6 integers allowed):"))
            if i == 0:
                a = passwd
            if i == 1:
                if a == passwd:
                    print("password confirmed")
                    flag = False
                else:
                    print("password do not match")
                    flag = True

    query = "insert into users(name, lastname, passwd) values(%s,%s,%s)" % (
        name, lname, passwd)
    cursor.execute(query)  # cursor=get_Cursor()
    db.commit


def userauthentication():
    '''
    Gets account no., password and check in db
    returns user object
    '''

    flag = False
    cursor.execute("select * from users")  # cursor = get_Cursor()
    data = cursor.fetchall()

    while flag:  # user authentication
        acc = int(input("enter your accno"))
        passwd = int(input("enter your password"))

        for row in data:
            # checks every record from column 3(accno) with the users input
            if row[2] == acc and row[3] == passwd:
                flag = True
                break
            else:
                print("account no. or the password is wrong")
                break

    return flag  # returns true if user verified else false
