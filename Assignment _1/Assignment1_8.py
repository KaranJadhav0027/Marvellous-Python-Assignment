"""############################################################
    A program that accept Numbner from user and Display "*" on Screen

Input:
Enter a Number :5
OutPut:
*  *  *  *  *

Input:
Enter a Number :-5
OutPut:
*  *  *  *  *

###############################################################"""

def Display(No):
    if No<0 :
        No=No*-1    #for Convert into +ve to -ve
       #print("Enter Greater than 0(Zero) number") #

    for i in range(1,No+1,1):
        print("*",end="  ")
    
def main():

    print("Enter a Number :",end="")
    Value=int(input())
    Display(Value)

if __name__ == "__main__":
    main()