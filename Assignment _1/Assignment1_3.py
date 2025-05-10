"""############################################################
    A program that Contain Display Addition of Two Number 

Input :
Enter a First  Number :
11
Enter a Second Number :
5
OutPut:
Addtion of  11 And  5  is  16

###############################################################"""

def Add(No1,No2):
   return No1+No2
    

def main():
    print("Enter a First  Number :",end="")
    Value1=int(input())

    print("Enter a Second Number :",end="")
    Value2=int(input())
 
    Result=Add(Value1,Value2)
    print("Addtion of ",Value1 ,"And ",Value2," is ",Result)


if __name__ == "__main__":
    main()