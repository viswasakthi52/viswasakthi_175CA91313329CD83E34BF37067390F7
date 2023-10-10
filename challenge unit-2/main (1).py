class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = 4522128032
        self._account_holder_name = 'sakthivel '
        self._account_balance = 5001

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited {amount}. New balance: {self._account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew {amount}. New balance: {self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account balance for {self._account_holder_name}: {self._account_balance}")


if __name__ == "__main__":
    account_number = 4522128032
    account_holder_name ='sakthivel'
    initial_balance = 5001

    # Creating a new bank account instance
    my_account = BankAccount(account_number, account_holder_name, initial_balance)
    def bankaccound(self):
      print(f" BankAccount {self._account_number}:{self._account_holder_name}:{self._initial_balance}")

    while True:
        print(f"\n")
        print(f"BankAccount",(account_number, account_holder_name, initial_balance))
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            deposit_amount = float(input("Enter the deposit amount: "))
            my_account.deposit(deposit_amount)
        elif choice == "2":
            withdraw_amount = float(input("Enter the withdrawal amount: "))
            my_account.withdraw(withdraw_amount)
        elif choice == "3":
            my_account.display_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")