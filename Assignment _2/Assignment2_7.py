"""############################################################
    A program that accept a numnber and Display Pattern

Input:
Enter a  Number :5

Output:
         1       2       3       4       5
         1       2       3       4       5
         1       2       3       4       5
         1       2       3       4       5
         1       2       3       4       5

###############################################################"""

def Display(Value):
     if Value<0:
          Value=-Value
     for iCnt in range(Value):
           for jCnt in range(1,Value+1):
               print("\t",jCnt,end="")
           print()
         
def main():
     print("Enter a  Number :",end="")
     No1=int(input())

     Display(No1)

if __name__=="__main__":
    main()