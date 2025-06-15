import sys
from bank_account import BankAccount

def main():
    # Example starting balance for demonstration.
    # In a real application, you might load this from a database or file.
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command line argument: e.g., "deposit:50" -> ["deposit", "50"]
    parts = sys.argv[1].split(':')
    command = parts[0]
    
    # Safely get amount, if provided
    amount = None
    if len(parts) > 1:
        try:
            amount = float(parts[1])
        except ValueError:
            print(f"Error: Invalid amount '{parts[1]}'. Please enter a number.")
            sys.exit(1)

    if command == "deposit":
        if amount is not None:
            if account.deposit(amount):
                print(f"Deposited: ${amount:.2f}")
            # Error message for invalid amount is handled within deposit method
        else:
            print("Error: Deposit command requires an amount. Usage: deposit:<amount>")
    elif command == "withdraw":
        if amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Error: Withdraw command requires an amount. Usage: withdraw:<amount>")
    elif command == "display":
        if amount is not None: # Display command should not have an amount
            print("Error: Display command does not take an amount.")
            sys.exit(1)
        account.display_balance()
    else:
        print(f"Invalid command: '{command}'. Commands are: deposit, withdraw, display")

if __name__ == "__main__":
    main()