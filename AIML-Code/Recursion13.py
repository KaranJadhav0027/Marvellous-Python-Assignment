#input 4
#output:24
fact=1
def Factorial(no):
    global fact
    if(no>=1):
        fact=fact*no
        no=no-1
        Factorial(no)
    return fact

def main():
    ret=Factorial(4)
    print(ret)

if __name__=="__main__":
    main()