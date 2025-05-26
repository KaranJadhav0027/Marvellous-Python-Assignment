"""############################################################
  program creating Multiprocessing to Square list of number 

Input:
    data=[2,4,6,8,24,26,27,9,11,25]
Output:
  Square is : [4, 16, 36, 64, 576, 676, 729, 81, 121, 625]

###############################################################"""
import multiprocessing
import multiprocessing.pool

def Square(Value):
    # Sqr=1
    # Sqr=Value**2
    # return Sqr
    return Value**2

def main():

    data=[2,4,6,8,24,26,27,9,11,25]
    Ret=[]

    P=multiprocessing.Pool()
    Ret=P.map(Square,data)
    
    P.close()
    P.join()
    print("Square is :",Ret)


if __name__=="__main__":
    main()