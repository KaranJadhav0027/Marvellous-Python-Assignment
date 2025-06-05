
def CalculatePer(Obtained=400,Total=500):  
    Result=((Obtained/Total)*100)
    return Result

def main():                       
    #print("Enter Total Marks :")
    #Value1=int(input())

   # print("Enter Obtained Marks :")
   # Value2=int(input())

    output=CalculatePer(350,450)
    print("Percentage is :",output)

    output=CalculatePer(350)
    print("Percentage is :",output)

    output=CalculatePer()
    print("Percentage is :",output)

if __name__== "__main__":          
    main()