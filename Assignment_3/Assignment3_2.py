"""############################################################
    A program that accept a N numnber from user and store into 
    list Return maximum number in list

Input:
Number of Elements :7

Output:
Input Elements :
13
5
45
7
4
56
34
Maximun Number in list is : 56

###############################################################"""

def ListMax(Value):
    max=0
    for Cnt in Value:
        if max<Cnt:
            max=Cnt
    return max
                
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
    
    Ret=ListMax(Data)
    print("Maximun Number in list is :",Ret)

if __name__=="__main__":
    main()