class Account:
    def __init__(self,accountname,accountnumber,bankname,balance):
        self.accountname=accountname
        self.accountnumber=accountnumber
        self.bankname=bankname
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return f"Hello your current balance is Ksh.{self.balance}"

    def withdraw(self,amount_decrease):
        self.balance-=amount_decrease
        return f"Hello your balance is Ksh.{self.balance}"        