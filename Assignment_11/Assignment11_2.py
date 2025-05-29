"""############################################################
   Program  Recursion Function to print Factorial 

Input
Enter a Number :5

Output:
Factorial is :120
###############################################################"""

# def Factorial(no):
#     global fact
#     if no<0:
#         print("Enter Greater than Zero (0)")
#         return 0
#     fact=1
#     while (no>=1):
#         fact=fact*no
#         no=no-1
#         return fact

fact=1
def Factorial(no):
    global fact
    if no<0:
        print("Enter Greater than Zero (0)")
        return 0
    if(no>=1):
        fact=fact*no
        no=no-1
        Factorial(no)
    return fact

def main():
    print("Enter a Number :",end="")
    Value=int(input())

    ret=Factorial(Value)
    print("Factorial is :",ret)

if __name__=="__main__":
    main()