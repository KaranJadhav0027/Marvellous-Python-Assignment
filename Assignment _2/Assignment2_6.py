"""############################################################
    A program that accept a numnber and Display Pattern

Input:
Enter a  Number :5

OutPut:
        *       *       *       *       *
        *       *       *       *
        *       *       *
        *       *
        *

###############################################################"""

def Display(Value):
     if Value<0:
          Value=-Value
     for iCnt in range(Value,0,-1):
           for jCnt in range(iCnt):
               print("\t*",end="")
           print()
         
def main():
     print("Enter a  Number :",end="")
     No1=int(input())

     Display(No1)

if __name__=="__main__":
    main()