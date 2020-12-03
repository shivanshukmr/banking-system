from core.utils.mysqllogin import check_connection, get_mysql_credentials
from core.utils.info import balance, details, getusers, transactionHistory
from core.models.user import User
from core.utils.users import userauthentication, usercreation
from core.utils.transfers import deposit, withdraw, transfer
from core.assets.assets import colour, icon, bankcli_asciiart
from core.db.initialize import initialize_db
from tkinter import *
import os.path

#======main window=====
root = Tk()
root.title("Banking System")
root.configure(bg=colour)



credentials_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "core/db/mysqlcredentials.txt"
)
# if file doesn't exist
if not os.path.exists(credentials_path):
    get_mysql_credentials()
else:
    with open(credentials_path, "r") as f:
        output = [word.strip("\n") for word in f.readlines()]

    # if connection is unsuccessful
    if not check_connection(output[0], output[1], output[2], output[3]):
        get_mysql_credentials()
initialize_db()



user = None
while True:
    if isinstance(user, User):
        # signed in
        # if command == "help":
        #     print(help_signedin)
        # elif command == "transactionhistory":
        #     transactionHistory(user)
        # elif command == "balance":
        #     balance(user)
        # elif command == "details":
        #     details(user)
        # elif command == "showusers":
        #     getusers(user)
        # elif command == "deposit":
        #     deposit(user)
        # elif command == "withdraw":
        #     withdraw(user)
        # elif command == "signout":
        #     user = None
        #     print("You have signed out.")
        # elif command == "transfer":
        #     transfer(user)
        # elif command == "exit":
        #    break


    else:
        # # not signed in
        # if command == "help":
        #     print(help_notsignedin)
        # elif command == "createaccount":
        #     usercreation()
        # elif command == "signin":
        #     user = userauthentication()
        # elif command == "reconfigure":
        #     get_mysql_credentials()
        # elif command == "exit":
        #   break
root.mainloop()