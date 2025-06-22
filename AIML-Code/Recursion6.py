# Input :4
# Output: * * * *

def Display(no):
    for i in range(no):
        print("\t*",end="")

def main():
    Display(4)

if __name__=="__main__":
    main()