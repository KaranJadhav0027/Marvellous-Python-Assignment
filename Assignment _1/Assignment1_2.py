"""############################################################
    A program that Contain Display Even And Odd Number 

Input :Enter a Number :11
OutPut:
      11 is Odd Number

Input :Enter a Number :8
OutPut:
      8 is Even Number

###############################################################"""

def ChkNum(No):
    if No%2==0 :
        print(No,"is Even Number")
    else:
        print(No,"is Odd Number")
    

def main():
    print("Enter a Number :",end="")
    Value=int(input())

    ChkNum(Value)


if __name__ == "__main__":
    main()