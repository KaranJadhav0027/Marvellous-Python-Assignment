import threading
import time

def SumEven(no):
    sum=0
    for i in range(2,no+1,2):
        sum=sum+i
    print(sum)

def SumOdd(no):
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print(sum)

def main():

    print("Demonstraction of Serial Execution")

    start_time =time.time()
    SumEven(90000000)
    SumOdd(90000000)
    end_time=time.time()

    print("time required for execution is :",end_time-start_time)
    
    print("End of Main")

if __name__=="__main__":
    main()