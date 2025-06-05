from MarvellousFMR import filterX,mapX,reduceX

CheckEven= lambda No:(No%2==0)  
Increase=lambda No:(No+1)
Sum=lambda A,B:(A+B)

def main():

    Data=[]
    print("Enter Number of Elements :")
    Size=int(input())

    print("Please enter Numberic Value :")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input data :",Data)

    FData=list(filterX(CheckEven,Data))
    print("Filter Output :",FData)

    MData=list(mapX(Increase,FData))
    print("Map OutPut :",MData)

    RData=reduceX(Sum,MData)
    print("Reduce Outpur :",RData)

if __name__=="__main__":
    main()
