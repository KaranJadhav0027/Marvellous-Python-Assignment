"""############################################################

Enter First Value :12
Enter Second Value :5

Addition is : 17

Substration is : 7

Multiplaction is : 60

Division  is : 2

###############################################################"""

class Calculator:

    def __init__(self):
        self.No1=0
        self.No2=0

    def Accept(self):
        print("Enter First Value :",end="")
        self.No1=int(input())

        print("Enter Second Value :",end="")
        self.No2=int(input())

    def Add(self):
        return self.No1+self.No2
    
    def subtract(self):
        return self.No1-self.No2
    
    def Multiply(self):
        return self.No1*self.No2
    
    def Divide(self):
        if self.No2>0:
          return self.No1//self.No2
        else:
            return 0

def main():
    obj=Calculator()
    obj.Accept()

    Ret=obj.Add()
    print("Addition is :",Ret)

    Ret=obj.subtract()
    print("Substration is :",Ret)

    Ret=obj.Multiply()
    print("Multiplaction is :",Ret)

    Ret=obj.Divide()
    print("Division  is :",Ret)

if __name__=="__main__":
    main()