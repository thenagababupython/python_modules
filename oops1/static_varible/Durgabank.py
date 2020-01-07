import sys
class Customer:
    """customer class with bank operation"""
    bankname="DURGABANK"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after withdraw",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficent Funds Can't Perform this operation")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance after withdrawn",self.balance)
print("Welcome to customere",Customer.bankname)
name=input("Enter your  Name:")
c=Customer(name)
while True:
    print("d-Deposit\nw-Withdraw\ne-exit")
    option=input("choose your option:")
    if option=='d' or option=='D':
        amt=float(input("enter your Amout:"))
        c.deposit(amt)
    elif option=='w' or option=='D':
        amt=float(input("Enter your Amout:"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks For Banking")
        sys.exit()
    else:
        print("Invalid Option..Plz Choose Valid Banking")

