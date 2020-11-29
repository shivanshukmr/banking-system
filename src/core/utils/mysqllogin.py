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



def get_mysql_credentials():
    print("\nMySQL login credentials.\n")
    while True:
        host_ = input("Enter hostname (default localhost):") or "localhost"
        if host_ == "0":
            sys.exit(0)
        port_ = input("Enter port number (default 3306):") or "3306"
        user_ = input("Enter username (default root):") or "root"
        passwd_ = getpass("Enter password:")

        if check_connection(host_, port_, user_, passwd_):
            print("Successfully connected to MySQL server.")
            break

        print("Unable to connect to MySQL server.\n")
        print("Enter 0 to exit.\n")

    # write file
    credentials_path = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
        "db/mysqlcredentials.txt",
    )
    with open(credentials_path, "w") as f:
        f.write(host_ + "\n" + port_ + "\n" + user_ + "\n" + passwd_ + "\n")
