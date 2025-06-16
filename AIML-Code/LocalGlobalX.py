
no=11

def fun():
    global no
    print("inside Fun")
    x=21
    print("Value of X :",x)  #21
    no=no+1
    print("Value of No :",no) #12

def main():
    print("Value of No before fun :",no)#11
    fun()
    print("Value of No After fun :",no)#12
    
if __name__=="__main__":
    main()