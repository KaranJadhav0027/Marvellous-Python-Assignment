def Multiplication(Value1,Value2):
    result=Value1*Value2
    return result

def main():
    print("Enter First Number")
    No1=int(input())

    print("Enter Second Number")
    No2=int(input())

    Ans=Multiplication(No1,No2)

    print("Multiplication is :",Ans)

if __name__=="__main__":
     main()