"""############################################################
  Program Accept List And using Filter() keep only even number

Input:
Enter a Number :6
1
2
3
4
5
6
Output:
Even Number List : [2, 4, 6]
###############################################################"""

EvenData=lambda Value:Value%2==0

def main():
    print("Enter a Number :",end="")
    size=int(input())

    Data=[]
    for i in range(size):
        no=int(input())
        Data.append(no)
   
    MData=list(filter(EvenData,Data))
    print("Even Number List :",MData)
     
     
if __name__=="__main__":
    main()