from gui.Assets.assets import colour, box, font_c
import mysql.connector
import os.path
import sys
from tkinter import Label, Button, Toplevel


def check_connection(host_, port_, user_, passwd_):
    try:
        con = mysql.connector.connect(
            host=host_, port=port_, user=user_, passwd=passwd_
        )
        return True
    except Exception:
        return False


def get_mysql_credentials(self):
    newwindow = Toplevel(self)
    newwindow.title("MySQL Credentials")
    newWindow.geometry("500x500")
    while True:
        credential_title = Label(
            self, text="MySQL Login Credentials", bg=colour, fg=font_c
        )
        host_l = Label(self, text="Enter hostname", bg=colour, fg=font_c)
        port_l = Label(self, text="Enter port number", bg=colour, fg=font_c)
        user_l = Label(self, text="Enter username", bg=colour, fg=font_c)
        pass_l = Label(self, text="Enter password ", bg=colour, fg=font_c)

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
        check_button = Button(
            sef,
            text="Check",
            command=lambda: check_connection(
                host_e.get(), port_e.get(), user_e.get(), pass_e.get()
            ),
        )
        a = [
            "Could not connect to MySQL server. Please try again.",
            "Successfully connected to MySQL server.",
        ]
        if check_button == False:
            check = Label(self, text=a[0])
            check.grid(row=9, column=1, columnspan=2)

        else:
            check.grid_forget()
            check = Label(self, text=a[1])
            check.grid(row=9, column=1, columnspan=2)
            exit_button = Button(self, text="Done", command=quit)
            break

    # write file
    credentials_path = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
        "db/mysqlcredentials.txt",
    )
    with open(credentials_path, "w") as f:
        f.write(host_e.get() + "\n" + port_ + "\n" + user_ + "\n" + passwd_ + "\n")
