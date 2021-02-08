# this might look broken but this works
bankcli_asciiart = """  ____                    _       ____   _       ___
 | __ )    __ _   _ __   | | __  / ___| | |     |_ _|
 |  _ \\   / _` | | '_ \\  | |/ / | |     | |      | |
 | |_) | | (_| | | | | | |   <  | |___  | |___   | |
 |____/   \\__,_| |_| |_| |_|\\_\\  \\____| |_____| |___|
"""

help_signedin = """
Commands:
    help                    : Show this help message and exit
    transfer                : Transfer money
    deposit                 : Deposit money
    withdraw                : Withdraw money
    details                 : Show all bank details
    balance                 : Show current balance
    transactionhistory      : Show transaction history
    showusers               : Show other accounts
    delete                  : Delete account
    signout                 : Signout
    exit                    : Exit
"""

help_notsignedin = """
Commands:
    help                    : Show this help message and exit
    signin                  : Sign in to your bank account
    createaccount           : Create a new bank account
    reconfigure             : Reconfigure MySQL login credentials
    exit                    : Exit
"""
