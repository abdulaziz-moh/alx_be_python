import sys 
import os
the_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(the_path)
from programming_paradigm.bank_account import BankAccount

newacc = BankAccount(100)
newacc.deposit(100)
# newacc.display_balance()

if len(sys.argv) < 2:
    print("Please enter a command with a format like this below: ")
    print("python alx_be_python\\Exercise\\week6` bankaccount` main-0` exercise.py  <command>:<amount>")
    print("The commands we have: deposit, withdraw, display(note: display has no ammount section)")
    sys.exit()
    # NOTE: ESCAPE CHARACTER IN WINDOWS 11 power shell is this `(named backtick character) and in bash(for unix based os like git bash) it is \(backward slash).

    # python alx_be_python\\Exercise\\week6\ bankaccount\ main-0\ exercise.py deposit:500 withdraw:1000  # for bash
    # python alx_be_python\\Exercise\\"week6 bankaccount main-0 exercise.py" deposit:100    # this also work for bash (that is putting the name which have space inside a double quotation mark(not single quotation mark.))
    # python alx_be_python\\Exercise\\week6` bankaccount` main-0` exercise.py deposit:500 withdraw:1000  # for powershell


amount = None
parts = sys.argv[1].split(":")
if len(parts) > 1:
    try:
        amount = float(parts[1])
    except ValueError:
        print("Please enter number in the amount section!! ")
        sys.exit()
match parts[0]:
    case "deposit":
        if amount:
            newacc.deposit(amount)
            print(f"${amount:.2f} deposited succesfully. ")
            newacc.display_balance()
        else:
            print("Please enter amount to deposit!!")

    case "withdraw":
        if amount:
            if newacc.withdraw(amount):
                print(f"${amount} withdrawed succesfully. ")
                newacc.display_balance()

            else:
                print("Insufficient fund!! ")
        else:
            print("Please enter amount to withdraw!! ")

    case "display":
        newacc.display_balance()

    case __:
        print("Unkown command!! please try again with valid command")
        sys.exit()
    

