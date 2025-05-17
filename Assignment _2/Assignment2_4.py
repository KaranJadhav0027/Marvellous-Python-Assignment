"""############################################################
    A program that accept a numnber and Display Factorial Addition

Input:
Enter a  Number :12

Output:
Factors Addition is  12  is : 16

###############################################################"""

def Display(Value):
     if Value<0:
          Value=-Value

     Ans=0
     for Cnt in range(1,Value):
          if Value%Cnt==0:
               Ans=Ans+Cnt

     return Ans

          
def main():
     print("Enter a  Number :",end="")
     No1=int(input())

     Ret=Display(No1)
     print("Factors Addition is ",No1," is :",Ret)

if __name__=="__main__":
    main()