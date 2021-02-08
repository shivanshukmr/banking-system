import tkinter as tk
from tkinter import *
from tkinter import ttk


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


def authenticate():
    cursor = get_Cursor()
    cursor.execute("select * from users")  # cursor = get_Cursor()
    data = cursor.fetchall()
    if fname == "" or accno == "" or passwd == "" or con_pass == "":
        messagebox.OK("Alert", "All fields required")
    else:
        if passwd == con_pass:
            for row in data:
                # checks every record from column 3(accno) with the users input
                if row[2] == accno and row[3] == passwd:
                    login["state"] = "NORMAL"
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

    fname_l = Label(
        self,
        text="Your firstname",
    )
    accno_l = Label(
        self,
        text="Your account number",
    )
    passwd_l = Label(
        self,
        text="Enter your password",
    )
    confirmpass_l = Label(
        self,
        text="Confirm password",
    )

    fname_l.grid(row=1, column=0)
    accno_l.grid(row=2, column=0)
    passwd_l.grid(row=3, column=0)
    confirmpass_l.grid(row=4, column=0)

    fname_e = Entry(self, width=50)
    accno_e = Entry(self, width=50)
    passwd_e = Entry(self, width=50)
    confirmpass_e = Entry(self, width=50)

    fname_e.grid(row=1, column=1)
    accno_e.grid(row=2, column=1)
    passwd_e.grid(row=3, column=1)
    confirmpass_e.grid(row=4, column=1)

    global fname
    global accno
    global passwd
    global con_pass
    global login

    fname = fname_e.get()
    accno = accno_e.get()
    passwd = passwd_e.get()
    con_pass = confirmpass_e.get()

    # Check button
    login = Button(self, text="Login", state=DISABLED)
    login.grid(row=6, column=1, columnspan=2)

    check_b = Button(self, text="Check", command=authenticate())
    check_b.grid(row=5, column=1, columnspan=2)


def main_screen(root):
    main_screen = frame(
        root
    )  # create a GUI window  # set the configuration of GUI window
    main_screen.title("Account Login")
    main_screen.configure(bd=4, relief=RAISED, padx=5, pady=2)
    main_screen.grid(padx=2, pady=1, sticky=W + E)
    userauthentication()


# def title_screen(root):
#     frame1 = Frame(root)
#     frame1.configure(bd=4, relief=RAISED, padx=5, pady=2)
#     frame1.grid(padx=2, pady=1, sticky=W + E)
#     title_image = Label(frame1, text="BANK CLI")
#     title_image.pack()
#     version = Label(
#         frame1,
#         text="version 2.0",
#         anchor=W,
#         padx=2,
#         pady=5,
#     )
#     version.grid(row=2, column=1, columnspan=3, sticky=W + E)


root = tk.Tk()
root.title("Banking System")
root.iconbitmap("src\icon2.ico")
# title_screen(root)
main_screen(root)

# tabControl = ttk.Notebook(root)
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
# tab3 = ttk.Frame(tabControl)
# tab4 = ttk.Frame(tabControl)
# tab5 = ttk.Frame(tabControl)

# tabControl.add(tab1, text="welcome")
# tabControl.add(tab2, text="transfer money")
# tabControl.add(tab3, text="Change your information")
# tabControl.add(tab4, text="change passwod")
# tabControl.add(tab5, text="transaction history")
# tabControl.pack(expand=1, fill="both")
# ttk.Label(tab1, text="Welcome to bank CLI").grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab2, text="Transfer money").grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab3, text="change your info").grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab4, text="change your password").grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab5, text="transaction history").grid(column=0, row=0, padx=30, pady=30)
root.mainloop()
