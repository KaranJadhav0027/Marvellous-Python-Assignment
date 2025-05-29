"""############################################################
  Program Contain lambda function which accept Two number Returm Product

Input:
Enter First Number :4
Enter Second Number :3

Output:
Multiplication is using Lambda : 12
Multiplication is using Class  : 12
Multiplication is : 12
###############################################################"""

MultiLambda=lambda Value1,Value2:Value1*Value2

class MultiClass:
    def __init__(self ,Value1,Value2):
        self.Value1=Value1
        self.Value2=Value2
 
    def MultiX(self):
        return self.Value1*self.Value2

class Multi:
    def __init__(self):
        self.MultiX=lambda i,j:i*j

def main():
    print("Enter First Number :",end="")
    No1=int(input())

    print("Enter Second Number :",end="")
    No2=int(input())

    Ret=MultiLambda(No1,No2)
    print("Multiplication is using Lambda :",Ret)

    PLobj=MultiClass(No1,No2)
    Ret=PLobj.MultiX()
    print("Multiplication is using Class  :",Ret)

    pobj=Multi()
    Ret=pobj.MultiX(No1,No2)
    print("Multiplication is :",Ret)

   
if __name__=="__main__":
    main()