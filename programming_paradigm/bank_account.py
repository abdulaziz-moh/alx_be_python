class BankAccount:
    """
    A simple bank account class that encapsulates banking operations.
    """
    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount must be a positive number.")
            return False
        self.account_balance += amount
        return True

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if funds were sufficient and withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")