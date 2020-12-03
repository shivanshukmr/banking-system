from getpass import getpass
import mysql.connector
import os.path
import sys
from tkinter import *


def check_connection(host_, port_, user_, passwd_):
    try:
        con = mysql.connector.connect(
            host=host_, port=port_, user=user_, passwd=passwd_
        )
        return True
    except Exception:
        return False


def get_mysql_credentials():
    print("\nMySQL login credentials.\n")
    while True:
        # host_ = input("Enter hostname (default localhost):") or "localhost"
        # if host_ == "0":
        #     sys.exit(0)
        # port_ = input("Enter port number (default 3306):") or "3306"
        # user_ = input("Enter username (default root):") or "root"
        # passwd_ = getpass("Enter password:")

        # if check_connection(host_, port_, user_, passwd_):
        #     print("Successfully connected to MySQL server.")
        #     break

        # print("Unable to connect to MySQL server.\n")
        # print("Enter 0 to exit.\n")
        host_l = Label(self, text="Enter hostname", bg="#0859c6", fg="White")
        port_l = Label(self, text="Enter port number", bg="#0859c6", fg="White")
        user_l = Label(self, text="Enter username", bg="#0859c6", fg="White")
        pass_l = Label(self, text="Enter password ", bg="#0859c6", fg="White")

        host_l.grid(row=5, column=1)
        port_l.grid(row=6, column=1)
        user_l.grid(row=7, column=1)
        pass_l.grid(row=8, column=1)

        host_e = Entry(self, width=50, bg="#badbff")
        host_e.insert(0, "locahost")
        port_e = Entry(self, width=50, bg="#badbff")
        port_e.insert(0, "3306")
        user_e = Entry(self, width=50, bg="#badbff")
        user_e.insert(0, "root")
        pass_e = Entry(self, width=50, bg="#badbff", elide=True)

        host_e.grid(row=5, column=2)
        port_e.grid(row=6, column=2)
        user_e.grid(row=7, column=2)
        pass_e.grid(row=8, column=2)

        if check_connection(host_e.get(), port_e.get(), user_e.get(), pass_e.get()):
            check = Label(self, text="Successfully connected to MySQL server.")
            break

    # write file
    credentials_path = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
        "db/mysqlcredentials.txt",
    )
    with open(credentials_path, "w") as f:
        f.write(host_ + "\n" + port_ + "\n" + user_ + "\n" + passwd_ + "\n")
