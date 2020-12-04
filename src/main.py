from core.utils.mysqllogin import check_connection, get_mysql_credentials
from core.utils.info import balance, details, getusers, transactionHistory
from core.models.user import User
from core.utils.users import userauthentication, usercreation
from core.utils.transfers import deposit, withdraw, transfer
from core.assets.assets import colour, font_c, icon, bankcli_asciiart
from core.db.initialize import initialize_db
from tkinter import *
import os.path

# ======main window=====
root = Tk()
root.title("Banking System")
root.configure(bg=colour)
root.iconbitmap(icon)
title_image = Label(root,image=bankcli_asciiart)
title_image.pack()
version = Label(root, text="version 2.0", bg=colour, fg=font_c)
version.grid(row=2, column=1)


#======credentials check=====
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


#=====functions========
user = None
while True:
    if isinstance(user, User):
        # signed in
    else:
        # # not signed in
root.mainloop()