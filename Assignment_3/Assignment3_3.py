"""############################################################
    A program that accept a N numnber from user and store into 
    list Return minimum number in list

Input:
Number of Elements :4

Output:
Input Elements :
2
5
6
3
Minimun Number in list is : 2
###############################################################"""

def ListMin(Value):
    min=Value[0]
    for Cnt in Value:
        if min>Cnt:
            min=Cnt
    return min
                
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
    
    Ret=ListMin(Data)
    print("Minimun Number in list is :",Ret)

if __name__=="__main__":
    main()