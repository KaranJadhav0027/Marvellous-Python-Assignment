"""############################################################
    A program that accept two numnber And Perform Arithmetic Operation

Input:
Enter a First Number :11
Enter a Second Number :3

Output:print("Enter a Name :",end="")
     No1=(input())
Addition is : 14
Subtraction is : 8
Multiplication is : 33
Division is : 3.6666666666666665

###############################################################"""

from Arithematic import *

def main():
     print("Enter a First Number :",end="")
     No1=int(input())

     print("Enter a Second Number :",end="")
     No2=int(input())

     Ret=Add(No1,No2)
     print("Addition is :",Ret)

     Ret=Sub(No1,No2)
     print("Subtraction is :",Ret)

     Ret=Mult(No1,No2)
     print("Multiplication is :",Ret)

     Ret=Div(No1,No2)
     print("Division is :",Ret)


if __name__=="__main__":
    main()