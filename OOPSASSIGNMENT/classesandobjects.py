class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        self.balance -= amount
    
    def check_balance(self):
        print(f"your net balance is {self.balance}")


bank1 = BankAccount("shivu12345","shivam purve",20_000)

bank1.deposit(5000)
bank1.withdraw(2000)

bank1.check_balance()

