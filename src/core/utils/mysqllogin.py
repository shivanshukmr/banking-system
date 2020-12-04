from core.assets.assets import colour, box
from getpass import getpass
import mysql.connector
import os.path
import sys


def check_connection(host_, port_, user_, passwd_):
    try:
        con = mysql.connector.connect(
            host=host_, port=port_, user=user_, passwd=passwd_
        )
        return True
    except Exception:
        return False

def check():
    
def get_mysql_credentials(self):
    while True:
        credential_title = Label(self, text="MySQL Login Credentials", bg=colour, fg="White")
        host_l = Label(self, text="Enter hostname", bg=colour, fg="White")
        port_l = Label(self, text="Enter port number", bg=colour, fg="White")
        user_l = Label(self, text="Enter username", bg=colour, fg="White")
        pass_l = Label(self, text="Enter password ", bg=colour, fg="White")

        credential_title.grid(row=4, column=1, columnspan=2)
        host_l.grid(row=5, column=1)
        port_l.grid(row=6, column=1)
        user_l.grid(row=7, column=1)
        pass_l.grid(row=8, column=1)

        host_e = Entry(self, width=50, bg=box)
        host_e.insert(0, "locahost")
        port_e = Entry(self, width=50, bg=box)
        port_e.insert(0, "3306")
        user_e = Entry(self, width=50, bg=box)
        user_e.insert(0, "root")
        pass_e = Entry(self, width=50, bg=box, elide=True)

        host_e.grid(row=5, column=2)
        port_e.grid(row=6, column=2)
        user_e.grid(row=7, column=2)
        pass_e.grid(row=8, column=2)
        check_button=Button(sef, text="Done", command=lambda: check_connection(host_e.get(), port_e.get(), user_e.get(), pass_e.get()))
        if check_button==True:
            check = Label(self, text="Successfully connected to MySQL server.")
            check.pack()
            break
        else:
            check = Label(self, text="Could not connect to MySQL server. Please try again.")
            check.pack()

    # write file
    credentials_path = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
        "db/mysqlcredentials.txt",
    )
    with open(credentials_path, "w") as f:
        f.write(host_e.get() + "\n" + port_ + "\n" + user_ + "\n" + passwd_ + "\n")
