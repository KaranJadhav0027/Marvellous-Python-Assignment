import os
import time
def fun(no):
    print("PID is :",os.getpid())
    sum=0
    for i in range(1,no):
        sum=sum+(i*i*i)
    return sum

def main():
    Start_Time=time.time()

    data=[100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    result=[]

    for i in data:
        result.append(fun(i))
    print(result)
    End_Time=time.time()

    print("Execution time is :",End_Time-Start_Time)
if __name__=="__main__":
    main()