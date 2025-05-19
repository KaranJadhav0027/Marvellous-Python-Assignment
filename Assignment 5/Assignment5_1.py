"""############################################################
  Program Contain Arithmetic Operation 
  
Input:
Enter First Number :3
Enter Second Number :6

Output:
Addition is : 9
Substraction is : -3
Multiplication is : 18
Division is : 0.5

Input:
Enter First Number :3
Enter Second Number :0

output:
Addition is : 3
Difference is : 3
Product is : 0
Division is : Enter Greater than Zero Value

###############################################################"""

# def Arithmetic(Value1,Value2):
    
#     Add=Value1+Value2
#     print("Addition is :",Add)

#     Sub=Value1-Value2
#     print("Substraction is :",Sub)

#     Multi=Value1*Value2
#     print("Multiplication is :",Multi)
    
#     if Value2==0:
#         print("Enter Greater than Zero Value")
#     Div=Value1/Value2
#     print("Division is :",Div)

ArithmeticSum=lambda Value1,Value2:Value1+Value2

ArithmeticDiff=lambda Value1,Value2:Value1-Value2

ArithmeticProduct=lambda Value1,Value2:Value1*Value2

ArithmeticDiv=lambda Value1,Value2:Value1/Value2 if Value2!=0 else 'Enter Greater than Zero Value'

def main():
    print("Enter First Number :",end="")
    No1=int(input())

    print("Enter Second Number :",end="")
    No2=int(input())
    
    Ret=ArithmeticSum(No1,No2)
    print("Addition is :",Ret)  

    Ret=ArithmeticDiff(No1,No2)
    print("Difference is :",Ret)  

    Ret=ArithmeticProduct(No1,No2)
    print("Product is :",Ret)  

    Ret=ArithmeticDiv(No1,No2)
    print("Division is :",Ret)  

if __name__=="__main__":
    main()