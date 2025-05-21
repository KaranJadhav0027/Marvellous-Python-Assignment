"""############################################################
  Program Accept List And using map() double each value

Input:
Enter a Number :5
1
2
3
4
26

Output:
Double List : [2, 4, 6, 8, 52]
###############################################################"""

Doubled=lambda Value:Value*2

def main():
    print("Enter a Number :",end="")
    size=int(input())

    Data=[]
    for i in range(size):
        no=int(input())
        Data.append(no)
   
    MData=list(map(Doubled,Data))
    print("Double List :",MData)
     
     
if __name__=="__main__":
    main()