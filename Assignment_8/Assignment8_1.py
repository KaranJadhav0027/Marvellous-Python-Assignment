"""############################################################
  program creating two thread which Display First 10 odd And Even Number

###############################################################"""

import threading

def Even():
    for i in range(2,21,2):
            print("Even :",i)

def Odd():
    for i in range(1,21,2):
            print("Odd :",i)
        
def main():
    
    T1=threading.Thread(target=Even)
    T2=threading.Thread(target=Odd)
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__=="__main__":
    main()