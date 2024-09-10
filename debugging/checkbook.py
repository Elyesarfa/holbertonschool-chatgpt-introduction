#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """
        Initialize a Checkbook instance with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook account.
        
        Parameters:
        amount (float): The amount to be deposited.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook account.
        
        Parameters:
        amount (float): The amount to be withdrawn.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook account.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook instance.
    It handles user input and performs actions such as deposit, withdraw, and check balance.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = float(input("Enter the amount to deposit: $").strip())
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $").strip())
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
