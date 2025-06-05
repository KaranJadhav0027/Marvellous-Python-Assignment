
CheckEven= lambda No:(No%2==0)  
Increase=lambda No:(No+1)
Sum=lambda A,B:(A+B)

def filterX(Task,Values):
    Result=[]
    for no in Values:
        Ret=Task(no)
        if(Ret==True):
            Result.append(no)
        #Result.append(Task(no)) #OR

    return Result

def mapX(Task,Values):
    Result=[]
    for no in Values:
       Ret=Task(no)
       Result.append(Ret)

    return Result

def reduceX(Task,Values):
    Result=0
    
    #[11, 13, 5, 7, 9, 13, 17]
    for no in Values:
        Result=Task(Result,no)

    return Result

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
