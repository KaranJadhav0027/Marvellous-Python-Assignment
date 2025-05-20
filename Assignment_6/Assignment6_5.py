"""############################################################
  Program Contain Check number is prime or not
 
Input:
Enter a number :11

output:
11 is prime number 
###############################################################"""

def CheckPrime(Value):
    if Value<0:
        print("Enter Greater than zero number")
        return

    Flag=False
    if Value==2:
        return 
    for i in range(2,Value-1):
        if (Value%i)==0:
            Flag=True
            break
            
    return Flag
                  
def main():
    print("Enter a number :",end="")
    No=int(input())

    Ret=CheckPrime(No)
    
    if Ret==True:
        print(No,"is not prime number")
    else:
        print(No,"is prime number")
    
if __name__=="__main__":
    main()