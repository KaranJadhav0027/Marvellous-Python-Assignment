def Addition(A,B):
    Result=0
    Result=A+B
    return Result

def main():
    print("Enter Firat Number :",end="")
    No1=int(input())

    print("Enter Second Number :",end="")
    No2=int(input())

    Ret=Addition(No1,No2)
    print("Addition is :",Ret)

if __name__=="__main__":
    main()