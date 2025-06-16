import os

def fun(no):
    sum=0
    for i in range(1,no):
        sum=sum+(i*i*i)
    return sum

def main():
    Ret=fun(10)
    print(Ret)
    
if __name__=="__main__":
    main()