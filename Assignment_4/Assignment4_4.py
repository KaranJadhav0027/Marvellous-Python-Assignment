"""############################################################
  Filter Map Reduce 
  
Input:
Number of Elements :10
Input Elements :
5
2
3
4
3
4
1
2
8
10

Output:
Input data : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
Filter Output : [2, 4, 4, 2, 8, 10]
Map OutPut : [4, 16, 16, 4, 64, 100]
Reduce Outpur : 204
###############################################################"""

from functools import reduce

def CheckEven(No):
       if No%2==0:
              return No
           
def Power(No):
            return No**2

def Addition(A,B):
            return A+B

def FMR(Value):
       
        print("Input data :",Value)

        FData=list(filter(CheckEven,Value))
        print("Filter Output :",FData)

        MData=list(map(Power,FData))
        print("Map OutPut :",MData)

        RData=reduce(Addition,MData)
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