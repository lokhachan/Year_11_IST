class SavingsAccount():
    def __init__(self, balance, account_id):
        self.__balance = balance
        self.__account_id = account_id

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.__balance:
                print("Sorry, you don't have enough in your account to do that.")
            else:
                self.__balance = self.__balance - amount
                print(f"You withdrew {withdrawal_amount}")
                print(f"New balance: {self.__balance}")
        else:
            print("Sorry, you can't withdraw negative money.")

my_account = SavingsAccount(1000, "FREER1234")

withdrawal_amount = int(input("How much would you like to withdraw? "))

my_account.withdraw(withdrawal_amount)