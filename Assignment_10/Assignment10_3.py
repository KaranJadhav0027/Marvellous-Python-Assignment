"""############################################################
  Filter Map Reduce 
  
Input:
Number of Elements :12
Input Elements :
4
34
36
76
68
24
89
23
86
90
45
70

Output:
Input data : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
Filter Output : [76, 89, 86, 90, 70]
Map OutPut : [86, 99, 96, 100, 80]
Reduce Outpur : 6538752000
###############################################################"""

from functools import reduce

def Check70To90(No):
       if (No>=70 and No<=90):
              return No
           
def Increase(No):
            return No+10
def Product(A,B):
            return A*B

def FMR(Value):
       
        print("Input data :",Value)

        FData=list(filter(Check70To90,Value))
        print("Filter Output :",FData)

        MData=list(map(Increase,FData))
        print("Map OutPut :",MData)

        RData=reduce(Product,MData)
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