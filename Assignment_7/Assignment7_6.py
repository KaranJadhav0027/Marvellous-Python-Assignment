"""############################################################
  Program Accept List And using Filter() find Prime  number

Input:
Enter a Number :8
10
11
12
13
14
15
16
17
Output:
Prime of List : [11, 13, 17]
###############################################################"""

# def CheckPrime(Value):
    
#     if Value==2 or Value==1:
#         return True
#     for i in range(2,Value-1):
#         if (Value%i)==0:
#             return False
#             break
#     return True

CheckPrime=lambda Value:Value==2 or Value==1 or all(Value%i !=0 for i in range(2,Value-1) )


def main():
    print("Enter a Number :",end="")
    size=int(input())

    Data=[]
    for i in range(size):
        no=int(input())
        Data.append(no)
   
    Ret=list(filter(CheckPrime,Data))
    print("Prime of List :",Ret)
     
     
if __name__=="__main__":
    main()