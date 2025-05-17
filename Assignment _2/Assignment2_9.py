"""############################################################
    A program that accept a numnber and Display Digit Count

Input:
Enter a  Number :5187934
Output:
Digit Count is  7

###############################################################"""

def DigitsCount(Value):
    if Value<0:
          Value=-Value 
    count = 0
    while Value > 0:
        Value=Value//10
        count =count+ 1
    return count
         
def main():
     print("Enter a  Number :",end="")
     No1=int(input())
     
     Ret=DigitsCount(No1)
     print("Digit Count is ",Ret)

if __name__=="__main__":
    main()