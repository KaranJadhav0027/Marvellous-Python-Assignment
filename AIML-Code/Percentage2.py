
def CalculatePer(Total,Obtained):  #3
    Result=((Obtained/Total)*100)
    return Result

def main():                       #2 
    print("Enter Total Marks :")
    Value1=int(input())

    print("Enter Obtained Marks :")
    Value2=int(input())

    output=CalculatePer(Value1,Value2) #Position Argument

    print("Percentage is :",output)

if __name__== "__main__":          #1 Start 
    main()