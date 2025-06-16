no=11

def fun(no1):
    #global no  #as karu naka
    print("Fun No :",no)
    
def main():
    print("Main No before fun :",no)#11
    fun(21)
    print("Value of No After fun :",no)#11
    
if __name__=="__main__":
    main()