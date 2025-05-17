"""############################################################
    A program that accept a numnber and Check number is prime or not

Input:
Enter a  Number :5

Output:
5 is Not Prime Number

###############################################################"""

def Display(Value):

     Ans=0
     for Cnt in range(1,Value):
          if Value%Cnt==0:
               print(Value," is Not Prime Number ")
               return
          else:
               print(Value,"It is  Prime Number")
       
def main():
     print("Enter a  Number :",end="")
     No1=int(input())

     Display(No1)
     
if __name__=="__main__":
    main()