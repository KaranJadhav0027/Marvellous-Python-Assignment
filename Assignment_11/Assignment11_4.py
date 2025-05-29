"""############################################################
   Program  Recursion Function to Display Power 

Input:
Enter a Number :2
Enter a Power :3

OutPut:
Power is : 8
###############################################################"""

# def PowerFunction(no,Pow):
#     Result=1
#     while Pow>0:
#         Result=Result*no
#         Pow=Pow-1
        
#     return Result
Result=1
def PowerFunction(no,Pow):
    global Result
    if Pow>0:
        Result=Result*no
        Pow=Pow-1
        PowerFunction(no,Pow)
        
    return Result

def main():
    print("Enter a Number :",end="")
    Value=int(input())

    print("Enter a Power :",end="")
    Power=int(input())

    ret=PowerFunction(Value,Power)
    print("Power is :",ret)

if __name__=="__main__":
    main()