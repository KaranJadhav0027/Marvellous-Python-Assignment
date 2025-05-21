"""############################################################
  Program Accept List And using reduce() find Product of all number

Input:
Enter a Number :3
2
3
4

output:
Product of  List : 24
###############################################################"""
from functools import reduce

Product=lambda Value1,Value2:Value1*Value2

def main():
    print("Enter a Number :",end="")
    size=int(input())

    Data=[]
    for i in range(size):
        no=int(input())
        Data.append(no)
   
    Ret=reduce(Product,Data)
    print("Product of  List :",Ret)
     
     
if __name__=="__main__":
    main()