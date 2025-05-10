"""############################################################
    A program that accept Name For user and Display length of its Name

Input:
Enter a Name :Marvellous
Output:
10
###############################################################"""

def Display(Name):
    
    count=0
    for i in Name:
           count=count+1
    return count
       # return len(Name)     
    
def main():

    print("Enter a Name :",end="")
    Value=(input())
    ret=Display(Value)

    print(ret)

if __name__ == "__main__":
    main()