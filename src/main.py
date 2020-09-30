from core.models.user import User
from core.models import menu_txt
user = None
while True:
    # menu here
    print("Type 'help' to see the list of commands")
    if isinstance(user, User):
        # signed in
        command = input()
        if command == "help":
            print(line1)

        pass
    else:
        # not signed in
        command = input()
        if command == "help":
            print(line2)
        pass
    break
