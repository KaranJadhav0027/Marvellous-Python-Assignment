"""############################################################
  Program Accept 5 number and find Largest number

Input:
Enter 5 number :
23
89
12
56
45
Output:
Maximun number is : 89
###############################################################"""

def CheckMax(ListValue):
    Max=ListValue[0]

    for Cnt in ListValue:
        if Cnt > Max:
            Max=Cnt
    return Max
    
def main():
    data=[]
    print("Enter 5 number :")
    for i in range(5):
        No=int(input())
        data.append(No)

    Ret = CheckMax(data)
    print("Maximun number is :",Ret)
    
if __name__=="__main__":
    main()