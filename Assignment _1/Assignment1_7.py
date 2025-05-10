"""############################################################
    A program that accept Numbner from user and Check Its Divisible By 5 or Not

Input:
Enter a Number :25
OutPut:
25 is Devisible by 5

Input:
Enter a Number :8
OutPut:
8 is not Devisible by 5

###############################################################"""

def Display(No):
    
    if No%5==0 :
       return True
    else:
       return False
     
def main():

    print("Enter a Number :",end="")
    Value=int(input())
    
    Ret=Display(Value)

    if Ret==True:
        print(Value,"is Devisible by 5")
    else:
        print(Value,"is not Devisible by 5")

if __name__ == "__main__":
    main()