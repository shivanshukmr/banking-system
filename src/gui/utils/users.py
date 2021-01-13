# get connection object and cursor object from dbconnector.connector
# user creation
# user authentication/signup
from core.db.connector import get_Cursor, get_DB
from core.tables.user import User
from gui.Assets.assets import colour, font_c, box
from tkinter import *
from tkinter import messagebox


#===========================create user=====================
def signup(accno):
    message = Label(self, text="New Account created", bg=colour, fg=font_c)
    message.grid(row=7, column=1, columnspan=2)
    acc_l = Label(self, text="Your account number is " + aacno, bg=colour, fg=font_c)
    acc_l.grid(row=8, column=1, columnspan=2)
    acc=int(accno)
    cursor.execute("select firstname from users where accno = %s", (acc,))
    firstname = cursor.fetchone()
    cursor.execute("select lastname from users where accno = %s", (acc,))
    lastname = cursor.fetchone()
    cursor.execute("select date_created from users where accno = %s", (acc,))
    datecreated = cursor.fetchone()
    cursor.execute("select balance from users where accno = %s", (acc,))
    balance = cursor.fetchone()
    # return User object
    return User(acc, firstname, lastname, datecreated, balance)
    
#password check function
def check(a, b, c, d):
    cursor = get_Cursor()
    db = get_DB()
    if (a == "" or b == "" or c == "" or d == ""):
        messagebox.OK("Alert", "All fields are required")
    else:
        if c == d:
            cursor.execute(
                "insert into users(firstname,lastname,passwd) values(:fname, :lname, :pass),"{'fname': fname.get(),'lname': lname.get(),'pass': passwd.get()}
            )  
            db.commit()

            #account number detail
            cursor.execute("select max(accno) from users;")
            acc = cursor.fetchone()
            accno=str(acc[0])
            signup = Button(self, text="Sign up", command=lambda: signup(accno))
            signup.grid(row=6, column=1, columnspan=2)
        else:
            return messagebox.showerror(
                "Password authentication", "Password does not match! Try again."
            )



def usercreation(self):
    """
    Gets name, password(twice), and updates db.
    user gets auto-generated accno.
    """
    import getpass
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
    check_b = Button(
        self, text="Check", command=lambda: check(fname, lname, passwd, con_pass)
    )
    check_b.grid(row=5, column=1, columnspan=2)

    signup = Button(self, text="Sign up", state=DISABLED)
    signup.grid(row=6, column=1, columnspan=2)

#==================login====================
def login(acc):
    cursor.execute("select firstname from users where accno = %s", (acc,))
    firstname = cursor.fetchone()
    cursor.execute("select lastname from users where accno = %s", (acc,))
    lastname = cursor.fetchone()
    cursor.execute("select date_created from users where accno = %s", (acc,))
    datecreated = cursor.fetchone()
    cursor.execute("select balance from users where accno = %s", (acc,))
    balance = cursor.fetchone()
    # return User object
    return User(acc, firstname, lastname, datecreated, balance)

def authenticate(a, acc, passwd, d):
    cursor = get_Cursor()
    cursor.execute("select * from users")  # cursor = get_Cursor()
    data = cursor.fetchall()
    if a == "" or acc == "" or passwd == "" or d == "":
        messagebox.OK("Alert", "All fields required")
    else:
        if passwd == d:
            for row in data:
            # checks every record from column 3(accno) with the users input
            if row[2] == acc and row[3] == passwd:
                login = Button(self, text="Login", command=lambda: login(acc))
                login.grid(row=6, column=1, columnspan=2)
            else:
                return messagebox.showerror(
                    "Password authentication", "Password do not match! Try again."
                )

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

    fname_l = Label(self, text="Your firstname", bg=colour, fg=font_c)
    accno_l = Label(self, text="Your account number", bg=colour, fg=font_c)
    passwd_l = Label(self, text="Enter your password", bg=colour, fg=font_c)
    confirmpass_l = Label(self, text="Confirm password", bg=colour, fg=font_c)

    fname_l.grid(row=1, column=0)
    accno_l.grid(row=2, column=0)
    passwd_l.grid(row=3, column=0)
    confirmpass_l.grid(row=4, column=0)
    
    fname_e = Entry(self, width=50, bg=box)
    accno_e = Entry(self, width=50, bg=box)
    passwd_e = Entry(self, width=50, bg=box)
    confirmpass_e = Entry(self, width=50, bg=box)


    fname_e.grid(row=1, column=1)
    accno_e.grid(row=2, column=1)
    passwd_e.grid(row=3, column=1)
    confirmpass_e.grid(row=4, column=1)

    fname = fname_e.get()
    lname = accno_e.get()
    passwd = passwd_e.get()
    con_pass = confirmpass_e.get()
    
    #Check button
    check_b = Button(
        self, text="Check", command=lambda: check(fname, lname, passwd, con_pass)
    )
    check_b.grid(row=5, column=1, columnspan=2)

    login = Button(self, text="Login", state=DISABLED)
    login.grid(row=6, column=1, columnspan=2)
