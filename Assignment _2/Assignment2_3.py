"""############################################################
    A program that accept a numnber and Factorial

Input:
Enter a  Number :5
Output:
Factorial of 5  is : 120

###############################################################"""

def Display(Value):
     if Value<0:
          Value=-Value

     Ans=1
     for Cnt in range(1,Value+1):
          Ans=Ans*Cnt
     return Ans

          
def main():
     print("Enter a  Number :",end="")
     No1=int(input())

     Ret=Display(No1)
     print("Factorial of",No1," is :",Ret)

if __name__=="__main__":
    main()