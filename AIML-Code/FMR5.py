def Increase(A):
    return A+1

def Demo(Taks,Value):
    Result=[]

    for No in Value:
        ret=Taks(No)
        Result.append(ret)
    return Result
        
Data=[13,17,10,14,11]

RData=list(Demo(Increase,Data))

print(RData)