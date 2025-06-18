
def CalculatePer(Total,Obtained):  
    Result=((Obtained/Total)*100)
    return Result

def main():                       
    print("Enter Total Marks :")
    Value1=int(input())

    print("Enter Obtained Marks :")
    Value2=int(input())

    output=CalculatePer(Value1,Value2) #Position Argument

    print("Percentage is :",output)

if __name__== "__main__":          
    main()