"""############################################################
Enter a number :12

12 is a Prime Number : False

12 is a Perfect Number : False

1 2 3 4 6 12

12 Summation of Factors is : 28

###############################################################"""

class Numbers:
   
    def __init__(self,no):
        self.No=no
    
    def ChkPrime(self):
        if self.No==2 or self.No==1:
            return True
        for i in range(2,self.No//2):
            if self.No%i!=0:
                return True
            else:
                return False
            
    def ChkPerfect(self):
        per=1
        for i in range(2,self.No):
            if self.No%i==0:
                per=per+i
        if per==self.No:
            return True
        else:
            return False

    def SumFactors(self):
        FactSum=1
        for i in range(2,self.No+1):
            if self.No%i==0:
                FactSum=FactSum+i
        return FactSum

    def Factors(self):
        for i in range(1,self.No+1):
            if self.No%i==0:
                print(i,end=" ")
        print()

        
def main():
    print("Enter a number :",end="")
    Value=int(input())

    nobj=Numbers(Value)
    Ret =nobj.ChkPrime()
    print(Value,"is a Prime Number :",Ret)

    Ret=nobj.ChkPerfect()
    print(Value,"is a Perfect Number :",Ret)

    nobj.Factors()

    Ret=nobj.SumFactors()
    print(Value,"Summation of Factors is :",Ret)
    
if __name__=="__main__":
    main()