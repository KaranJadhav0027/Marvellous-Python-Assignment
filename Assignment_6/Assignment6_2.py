"""############################################################
  Program Contain Sum of  1 to 100 Even number using loop
  
OutPut:
Sun of Even number between 1 to 100 is : 2550
###############################################################"""

def SumEven():
    i=1
    sum=0
    while(i<=100):
        if i%2==0:
           sum=sum+i
        i=i+1
    return sum

def main():
    Ret =SumEven()
    print("Sun of Even number between 1 to 100 is :",Ret)  
 
if __name__=="__main__":
    main()