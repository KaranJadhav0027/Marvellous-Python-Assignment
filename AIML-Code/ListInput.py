
def main():
    print("Enter number of Element :")
    size=int(input())

    Data=list()

    print("Enter the Value :")
    for i in range(size):
        no=int(input())
        Data.append(no)

    print("Enter elements are :")
    for Value in Data:
        print(Value)

        #addtion
        #even
        #odd
        #divisible

if __name__=="__main__":
    main()