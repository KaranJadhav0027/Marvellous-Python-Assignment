"""############################################################
  Program Contain check Largest among three Number
  
Input:
Enter First Number :5
Enter Second Number :3
Enter Third Number :9

output:
largest number is  9

###############################################################"""

def CheckMax(Value1,Value2,Value3):
    if Value1>Value2 and Value1>Value3:
        print("largest number is ",Value1)
       
    elif Value2>Value1 and Value2>Value3 :
        print("largest number is ",Value2)
    else:
        print("largest number is ",Value3)
    
def main():
    print("Enter First Number :",end="")
    No1=int(input())

    print("Enter Second Number :",end="")
    No2=int(input())

    print("Enter Third Number :",end="")
    No3=int(input())

    CheckMax(No1,No2,No3)
       

if __name__=="__main__":
    main()