# Input :4
# Output: * * * *

def Add(no):
    sum=0
    for i in range(1,no+1):
        sum=sum+i
    return sum

def main():
    ret=Add(4)
    print(ret)

if __name__=="__main__":
    main()