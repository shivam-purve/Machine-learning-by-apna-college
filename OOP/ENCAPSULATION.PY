class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        # self.balance = balance  #by default public accesible
        # self._balance  = balance  #protected accessible
        self.__balance =  balance #private accessible
    


    def get_balance(self):
        return self.__balance
    
    def set_balance(self,newBalance):
        self.__balance = newBalance
    



acc1 = BankAccount("Shivam purve",10_000)
acc1.set_balance(200_000)
#print(acc1.name,acc1.get_balance())  #by getter method

print(acc1.name,acc1._BankAccount__balance)