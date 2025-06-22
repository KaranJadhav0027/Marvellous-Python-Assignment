# Input :4
# Output: * * * *

def Display(no):
    if(no>=1):
        print("\t*",end="")
        no=no-1
        Display(no)

def main():
    Display(4)

if __name__=="__main__":
    main()