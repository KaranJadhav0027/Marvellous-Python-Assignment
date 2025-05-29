"""############################################################
  Program Contain class which accept one number and return 
  its 2nd Power

Input:
Enter the Number :4

Output:

4 Power is using Lambada : 16
4 Power is using class : 16
4 Power is : 16
###############################################################"""

PowerLambda=lambda Value:Value**2

class PowerClass:
    def __init__(self ,Value):
        self.Value=Value
 
    def PowerX(self):
        return self.Value**2

class Power:
    def __init__(self):
        self.PowerX=lambda i:i**2
        
def main():
    print("Enter the Number :",end="")
    No=int(input())

    Ret=PowerLambda(No)
    print(No,"Power is using Lambada :",Ret)

    PLobj=PowerClass(No)
    Ret=PLobj.PowerX()
    print(No,"Power is using class :",Ret)

    pobj=Power()
    Ret=pobj.PowerX(No)
    print(No,"Power is :",Ret)
   
if __name__=="__main__":
    main()