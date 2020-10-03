from core.assets.assets import bankcli_asciiart, help_notsignedin, help_signedin
from core.info import balance
from core.models.user import User
from core.users import userauthentication

user = None
firsttime = True

while True:
    if firsttime:
        # only print when its the first time
        print(bankcli_asciiart)
        print("BankCLI v1.0")
        print("Type 'help' to see the list of commands.\n")
        firsttime = False

    if isinstance(user, User):
        # signed in
        command = input(">> ")
        if command == "help":
            print(help_signedin)
        elif command == "balance":
            balance(user)
        elif command == "exit":
            break

    else:
        # not signed in
        command = input(">> ")
        if command == "help":
            print(help_notsignedin)
        elif command == "signin":
            user = userauthentication()
        elif command == "exit":
            break
