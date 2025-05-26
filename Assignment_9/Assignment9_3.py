"""############################################################
  program creating Multiprocessing to Factorial list of number 

Input:
    data=[2,4,6,8,24,26,27,9,11,25]
Output:
  Factorial is : [2, 24, 720, 40320, 620448401733239439360000,
    403291461126605635584000000, 10888869450418352160768000000, 362880, 39916800, 15511210043330985984000000]

###############################################################"""
import multiprocessing
import multiprocessing.pool

def Factorial(Value):
     Fact=1
     while Value>0:
         Fact=Fact*Value
         Value=Value-1
     return Fact

def main():

    data=[2,4,6,8,24,26,27,9,11,25]
    Ret=[]

    P=multiprocessing.Pool()
    Ret=P.map(Factorial,data)
    
    P.close()
    P.join()
    print("Factorial is :",Ret)


if __name__=="__main__":
    main()