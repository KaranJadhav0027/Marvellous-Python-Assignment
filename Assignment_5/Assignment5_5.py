"""############################################################
  Program Contain check Even and Odd number
  
Input:
Enter Number  :5

output
5 is an Odd Number

###############################################################"""

# def CheckEven(Value):
#     if Value%2==0:
#         return True
#     else:
#         return False

CheckEven=lambda Value:Value%2==0
    
def main():
    print("Enter Number  :",end="")
    No=int(input())

    Ret=CheckEven(No)
       
    if True==Ret:
        print(No,"is an Even Number")
    else:
        print(No,"is an Odd Number")

if __name__=="__main__":
    main()