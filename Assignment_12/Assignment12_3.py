"""############################################################

Enter First Number :98
Enter Second Number :4

Addition is : 102
Substraction is : 94
Multiplaction is : 392
Division is : 24.5

###############################################################"""

class Arithamatic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        print("Enter First Number :",end="")
        self.Value1=int(input())

        print("Enter Second Number :",end="")
        self.Value2=int(input())
        
    def Addition(self):
        return self.Value1+self.Value2
    
    def Substraction(self):
        return self.Value1-self.Value2
    
    def Multiplaction(self):
        return self.Value1*self.Value2

    def Division(self):
        if self.Value2==0:
            print("Enter Greather than Zero number")
            return
        return self.Value1/self.Value2

def main():
   
    Aobj=Arithamatic()
    Aobj.Accept()
    Ret=Aobj.Addition()
    print("Addition is :",Ret)

    Ret=Aobj.Substraction()
    print("Substraction is :",Ret)

    Ret=Aobj.Multiplaction()
    print("Multiplaction is :",Ret)

    Ret=Aobj.Division()
    print("Division is :",Ret)

if __name__=="__main__":
    main()