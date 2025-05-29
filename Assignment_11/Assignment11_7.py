"""############################################################
   Program  Recursion Function to print  Pattern 

Input
Enter a Number :4

Output:
*
*       *
*       *       *
*       *       *       *
###############################################################"""

# def Display(no):
#     i=1
#     while (i<=no):
#         print("*\t"*i)
#         i=i+1

# i=1
# def Display(no):
#     global i
#     if (i<=no):
#         print("*\t"*i)
#         i=i+1
#         Display(no)
       
# def Display(no):
#     i=1
#     while (i<=no):
#            j=1
#            while(j<=i):
#              print("*\t",end="")
#              j=j+1
#            print()
#            i=i+1

i=1
def Display(no):
    if no<0:
        print("Enter Greater than Zero (0)")
    global i
    if (i<=no):
           j=1
           while(j<=i):
             print("*\t",end="")
             j=j+1
           print()
           i=i+1
           Display(no)

def main():
    print("Enter a Number :",end="")
    Value=int(input())
    Display(Value)   

if __name__=="__main__":
    main()