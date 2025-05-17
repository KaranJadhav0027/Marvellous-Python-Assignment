"""############################################################
    A program that accept a N number from user and store into 
    list and Addition of prime number in list

Input:
Number of Elements :11
Input Elements :
13
5
45
7
4
56
10
34
2
5
8

Output:
Addition of Prime number in list is : 32
###############################################################"""
from MarvellousNum import chkPrime

def ListPrime(Value):
    Add=0
    for i in Value:
        if chkPrime(i):
            Add=Add+i

            print("##",Add)
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

    Ret=ListPrime(Data)
    print("Addition of Prime number in list is :",Ret)
   
    
if __name__=="__main__":
    main()