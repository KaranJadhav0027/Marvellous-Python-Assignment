
no=11

def fun():
    print("inside Fun")
    x=21
    print("Value of X :",x)  #21
    print("Value of No :",no) #11

def sun():
    print("inside Sun")
    y=51
    print("Value of Y :",y) #51
    print("Value of No :",no)  #11

def main():
    fun()
    sun()

if __name__=="__main__":
    main()