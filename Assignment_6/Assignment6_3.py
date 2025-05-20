"""############################################################
  Program Contain Multiplication table up to 10

Input:
Enter a number :7

OutPut:
|| 7 X 1  =|| 7
|| 7 X 2  =|| 14
|| 7 X 3  =|| 21
|| 7 X 4  =|| 28
|| 7 X 5  =|| 35
|| 7 X 6  =|| 42
|| 7 X 7  =|| 49
|| 7 X 8  =|| 56
|| 7 X 9  =|| 63
|| 7 X 10  =|| 70
###############################################################"""

def Table(Value):
    # if Value>10:
    #     print("Enter number between 1 to 10")

    for i in range(1,11):
        print("||",Value,"X",i," =||",Value*i)

def main():
    print("Enter a number :",end="")
    No=int(input())

    Table(No)
    
if __name__=="__main__":
    main()