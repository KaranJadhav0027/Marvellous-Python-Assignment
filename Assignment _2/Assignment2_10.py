"""############################################################
    A program that accept a numnber and Display Addition

Input:
Enter a  Number :5187934
Output:
Digit Addition is  37

###############################################################"""

def DigitsAdd(Value):
    if Value<0:
          Value=-Value 
    Add = 0
    while Value > 0:
        count=Value%10
        Add=Add+count
        Value = Value // 10
    return Add
         
def main():
     print("Enter a  Number :",end="")
     No1=int(input())
     
     Ret=DigitsAdd(No1)
     print("Digit Addition is ",Ret)

if __name__=="__main__":
    main()