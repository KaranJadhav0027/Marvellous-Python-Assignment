"""############################################################
    A program that accept a N numnber from user and store into 
    list Return addition os all elements list

Input:
Number of Elements :6

Output:
Input Elements :
13
5
45
7
4
56
Adddition of Number of Element is : 130

###############################################################"""

def ListAddition(Value):
    Add=0
    for Cnt in Value:
        Add=Add+Cnt
    return Add
                
def main():
    print("Number of Elements :",end="")
    size=int(input())
    # if size<0:
    #     print("Enter number grreater than zero()")

    if size<0:
        size=-size
    Data=list()

    print("Input Elements :")
    for i in range(size):
        no=int(input())
        Data.append(no)
    
    Ret=ListAddition(Data)
    print("Adddition of Number of Element is :",Ret)

if __name__=="__main__":
    main()