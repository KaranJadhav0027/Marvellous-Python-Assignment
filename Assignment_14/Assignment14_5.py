"""############################################################

Account No : 987654
Name : Karan
Balance Amount : 20000

Enter the Amount you want Deposit :23999

Enter the Amount you want Withdraw :3456

Account No : 987654
Name : Karan
Balance Amount : 40543

###############################################################"""

class BankAccount:
    def __init__(self,account_number,name,balance):
        self.Account_number=account_number
        self.Name=name
        self.Balance=balance
    
    def deposit(self):
        print("Enter the Amount you want Deposit :",end="")
        DAmount=int(input())
        self.Balance=self.Balance+DAmount

    def withdraw(self):
        print("Enter the Amount you want Withdraw :",end="")
        WAmount=int(input())
        if WAmount<self.Balance:
            self.Balance=self.Balance-WAmount
        else:
            print("Enter the less than ",self.Balance, "Amount")

    def DisplayBalance(self):
        print("Account No :",self.Account_number)
        print("Name :",self.Name)
        print("Balance Amount :",self.Balance)

def main():
   bobj=BankAccount(987654,"Karan",20000)
   bobj.DisplayBalance()
   bobj.deposit()
   bobj.withdraw()
   bobj.DisplayBalance()

if __name__=="__main__":
    main()