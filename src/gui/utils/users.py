# get connection object and cursor object from dbconnector.connector
# user creation
# user authentication/signin
from core.db.connector import get_Cursor, get_DB
from core.tables.user import User
from gui.Assets.assets import colour, font_c, box
from tkinter import *
from tkinter import messagebox

#password check function
def check(a, b):
    if a == b:
        return True

def usercreation(self):
    """
    Gets name, password(twice), and updates db.
    user gets auto-generated accno.
    """
    import getpass

    cursor = get_Cursor()
    db = get_DB()

    #get details
    fname_l = Label(self, text="Your firstname", bg=colour, fg=font_c)
    lname_l = Label(self, text="Your lastname", bg=colour, fg=font_c)
    passwd_l = Label(self, text="Enter a password", bg=colour, fg=font_c)
    confirmpass_l = Label(self, text="Confirm password", bg=colour, fg=font_c)

    fname_l.grid(row=1, column=0)
    lname_l.grid(row=2, column=0)
    passwd_l.grid(row=3, column=0)
    confirmpass_l.grid(row=4, column=0)
    
    fname_e = Entry(self, width=50, bg=box)
    lname_e = Entry(self, width=50, bg=box)
    passwd_e = Entry(self, width=50, bg=box)
    confirmpass_e = Entry(self, width=50, bg=box)


    fname_e.grid(row=1, column=1)
    lname_e.grid(row=2, column=1)
    passwd_e.grid(row=3, column=1)
    confirmpass_e.grid(row=4, column=1)

    fname = fname_e.get()
    lname = lname_e.get()
    passwd = passwd_e.get()
    con_pass = confirmpass_e.get()
    
    #Check button
    if fname=="" or lname=="" or passwd=="" or con_pass=="":
        check_b = Button(self, text="Done", state=DISABLED)
        check_b.grid(row=5, column=1, columnspan=2)
    else:
        check_b = Button(self, text="Done", command=lambda: check(passwd, con_pass))
        check_b.grid(row=5, column=1, columnspan=2)
        if check_b:
            cursor.execute(
                "insert into users(firstname,lastname,passwd) values(:fname, :lname, :pass),"
                {
                    'fname': fname.get(),
                    'lname': lname.get(),
                    'pass': passwd.get()
                }
            )  
            db.commit()
            message= Label(self, text="New Account created", bg=colour, fg=font_c)

            #account number detail
            cursor.execute("select max(accno) from users;")
            acc = cursor.fetchone()
            accno=str(acc[0])
            acc_l = Label(self, text="Your account number is " + aacno, bg=colour, fg=font_c)
        else:
            messagebox.showerror("Password authentication", "Password do not match! Try again.")


def userauthentication(self):
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
    acc = Label(self, text="Enter your account no.", bg=colour, fg=font_c)
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
