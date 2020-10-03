from core.assets.help_opts import help_notsignedin, help_signedin
from core.info import balance
from core.models.user import User
from core.users import userauthentication

user = None
firsttime = True


while True:
    # menu here
    if firsttime:
        # only print when its the first time
        # get asciiart
        with open("core/assets/asciiart.txt", "r") as f:
            asciiart = f.read()

        print(asciiart)
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

    else:
        # not signed in
        command = input(">> ")
        if command == "help":
            print(help_notsignedin)
        elif command == "signin":
            user = userauthentication()
