"""############################################################
  program creating two thread which Display Even and Odd Factor Sum

Input:
Enter a number :96

OutPut:
Even Factor Sum : 152
Odd Factor Sum : 3
Exit from Main
###############################################################"""
import threading

def EvenFactor(Value):
    ESum=0
    for i in range(1,Value):
        if Value%i==0:
            if i%2==0:
                ESum=ESum+i
    print("Even Factor Sum :",ESum)

def OddFactor(Value):
     OSum=0
     for i in range(2,Value):
        if Value%i==0:
            if i%2!=0:
                OSum=OSum+i
     print("Odd Factor Sum :",OSum)
                 
        
def main():
    print("Enter a number :",end="")
    No=int(input())

    T1=threading.Thread(target=EvenFactor,args=(No,))
    T2=threading.Thread(target=OddFactor,args=(No,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print("Exit from Main")

if __name__=="__main__":
    main()