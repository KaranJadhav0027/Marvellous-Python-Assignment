"""############################################################
   Program  Recursion Function to print 1 to N

Input
Enter a Number :5

Output
1
2
3
4
5
###############################################################"""

# def Display(no):
#     Rec=1
#     while (Rec<=no):
#         print(Rec)
#         Rec=Rec+1

Rec=1
def Display(no):
    global Rec
    if(Rec<=no):
        print(Rec)
        Rec=Rec+1
        Display(no)

def main():
    print("Enter a Number :",end="")
    Value=int(input())
    Display(Value)
   

if __name__=="__main__":
    main()