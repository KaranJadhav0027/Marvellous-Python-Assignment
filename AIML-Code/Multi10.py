import multiprocessing
import time
import os

def SumEven(no):
    print("PID sumEven task is ",os.getpid())  #500
    print("PID sumEven task is ",os.getppid()) #101
    sum=0
    for i in range(2,no+1,2):
        sum=sum+i
    print(sum)

def SumOdd(no):
    print("PID sumOdd task is ",os.getpid())#700
    print("PID sumOdd task is ",os.getppid())  #101
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print(sum)

def main():

    print("Demonstraction of Parallel Execution")
    print("PID main process is ",os.getpid())   #101
    start_time =time.time()
    P1=multiprocessing.Process(target=SumEven,args=(90000000,))
    P2=multiprocessing.Process(target=SumOdd,args=(90000000,))

    P1.start()
    P2.start()
    P1.join()
    P2.join()
    end_time=time.time()
 
    print("time required for execution is :",end_time-start_time)
    print("End of Main")

if __name__=="__main__":
    main()