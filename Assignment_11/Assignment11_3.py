"""############################################################
   Program  Recursion Function to Display DigitSum

Input
Enter a Number :1234

Output:
Digit Sum is : 10
###############################################################"""

# def DigitSum(no):
#     if no<0:
#         print("Enter Greater than Zero (0)")
#         return 0
#     DSum=0
#     while no!=0:
#         temp=no%10
#         DSum=DSum+temp
#         no=no//10
    
#     return DSum
DSum=0
def DigitSum(no):
    global DSum
    if no<0:
        print("Enter Greater than Zero (0)")
        return 0
   
    if no!=0:
        temp=no%10
        DSum=DSum+temp
        no=no//10
        DigitSum(no)
    return DSum

def main():
    print("Enter a Number :",end="")
    Value=int(input())

    ret=DigitSum(Value)
    print("Digit Sum is :",ret)

if __name__=="__main__":
    main()