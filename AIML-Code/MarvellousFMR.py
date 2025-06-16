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