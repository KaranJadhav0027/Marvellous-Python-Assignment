from functools import reduce

CheckEven= lambda No:(No%2==0)  

Increase=lambda No:(No+1)

Sum=lambda A,B:(A+B)

Data=[7,10,15,12,4,6,9,8,12,16]
print("Input data :",Data)

FData=list(filter(CheckEven,Data))
print("Filter Output :",FData)

MData=list(map(Increase,FData))
print("Map OutPut :",MData)

RData=reduce(Sum,MData)
print("Reduce Outpur :",RData)
