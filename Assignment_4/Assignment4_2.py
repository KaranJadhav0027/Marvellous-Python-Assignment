"""############################################################
  Program Contain lambda function which accept Two number Returm Product

Input:
Enter First Number :11
Enter Second Number :3

Output:
Multiplication is : 33
###############################################################"""

Power=lambda Value1,Value2:Value1*Value2

def main():
    print("Enter First Number :",end="")
    No1=int(input())

    print("Enter Second Number :",end="")
    No2=int(input())

    Ret=Power(No1,No2)
    print("Multiplication is :",Ret)

   
if __name__=="__main__":
    main()