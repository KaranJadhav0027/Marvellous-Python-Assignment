"""############################################################
    A program that Check whether that number is Positive or Negative or Zero  

Input:
Enter a Number :11
OutPut:
11 is Positive Number

Input:
Enter a Number :-8
OutPut:
-8 is Negative Number

Input:
Enter a Number :0
Output:
0 is Zero

###############################################################"""

def ChkNum(No):
    if 0<No:
        print(No,"is Positive Number")
    elif No==0:
        print(No,"is Zero")
    else:
        print(No,"is Negative Number")
    

def main():    
    print("Enter a Number :",end="") 
    Value=int(input())

    ChkNum(Value)


if __name__ == "__main__":
    main()