"""############################################################
    A program that accept a N number from user and store into 
    list Accept Another number from user and return frequency of that list

Input:
Number of Elements :11
Input Elements :
13
5
45
7
4
56
5
34
2
5
65
Element to Search :5

Output:
Frequency of  5  in list is : 3
###############################################################"""

def ListFrequency(Value,Fre):
    Count=0
    for Cnt in Value:
        if Fre==Cnt:
            Count=Count+1
    return Count
                
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

    print("Element to Search :",end="")
    No=int(input())
    
    Ret=ListFrequency(Data,No)
    print("Frequency of ", No," in list is :",Ret)

if __name__=="__main__":
    main()