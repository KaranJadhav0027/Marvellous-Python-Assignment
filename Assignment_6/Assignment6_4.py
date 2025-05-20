"""############################################################
  Program Contain Factorial using for loop
 
Input:
Enter a number :5

OutPut:
Factorial os  5  is : 120
###############################################################"""

def Factorial(Value):
    if Value<0:
        print("Enter Number Greater than Zero ")
    Fact=1
    for i in range(1,Value+1):
        Fact=Fact*i
    return Fact
    
        
def main():
    print("Enter a number :",end="")
    No=int(input())

    Ret=Factorial(No)
    print("Factorial os ",No," is :",Ret)
    
if __name__=="__main__":
    main()