# Task 1: Bank Account
class BankAccount:
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def displayAccount(self):
        print(f"Account No: {self.account_number}")
        print(f"Customer: {self.customer_name}")
        print(f"Balance: KSh {self.balance:.2f}")

if __name__ == "__main__":
    acc = BankAccount()
    acc.account_number = "1001"
    acc.customer_name = "Grace Achieng"
    acc.deposit(5000)
    acc.withdraw(2000)
    acc.displayAccount()
