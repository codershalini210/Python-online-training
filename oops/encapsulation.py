class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance 
    def deposite(self,amount):
        if(amount>0):
            self._balance = self._balance +amount
            return True
        return False
    def withdraw(self,amount):
        if(amount>0 and amount < self._balance):
            self._balance = self._balance - amount
            return True
        return False
    def getbalance(self):
        return self._balance
acc1 = Bankaccount('John',100)
acc1.deposite(50)   #balance will be 150
acc1.withdraw(60)   #balance will be 90
print("Current balance ", acc1._balance) # acc1.getbalance())