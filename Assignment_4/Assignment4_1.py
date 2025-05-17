"""############################################################
  Program Contain lambda function which accept one number and return 
  its 2nd Power

Input:
Enter the Number :-4

Output:
-4 Power is : 16
###############################################################"""

Power=lambda Value:Value**2

def main():
    print("Enter the Number :",end="")
    No=int(input())

    Ret=Power(No)
    print(No,"Power is :",Ret)

   
if __name__=="__main__":
    main()