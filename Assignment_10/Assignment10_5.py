"""############################################################
  Filter Map Reduce 
  
Number of Elements :8
Input Elements :
2
70
11
10
17
23
31
77

Input data : [2, 70, 11, 10, 17, 23, 31]
Filter Output : [2, 11, 17, 23, 31]
Map OutPut : [4, 22, 34, 46, 62]
Reduce Outpur :62
###############################################################"""

from functools import reduce

def CheckPrime(No):
       if No==2:
             return No
       for i in range(2,No):
             if No%i==0:
                return 
             
       return No
           
def Power(No):
            return No*2

def Maximum(A,B):
            if A>B:
                  return A
            else:
                  return B

def FMR(Value):
       
        print("Input data :",Value)

        FData=list(filter(CheckPrime,Value))
        print("Filter Output :",FData)

        MData=list(map(Power,FData))
        print("Map OutPut :",MData)

        RData=reduce(Maximum,MData)
        print("Reduce Outpur :",RData)

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

    FMR(Data)

   
if __name__=="__main__":
    main()