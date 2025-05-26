"""############################################################
  program creating thread thread which Dispaly 1 to 5 with Delay of 1 second

###############################################################"""
import threading
import time

def thread1():
    for i in range(6):
      time.sleep(1)
      print("Thread1 :",i)

def thread2():
    for i in range(6):
      time.sleep(1)
      print("Thread2 :",i)
    
def thread3():
    for i in range(6):
      time.sleep(1)
      print("Thread3 :",i)
                 
        
def main():
    
    T1=threading.Thread(target=thread1)
    T2=threading.Thread(target=thread2)
    T3=threading.Thread(target=thread3)
    T1.start()
    T2.start()
    T3.start()
    T1.join()
    T2.join()
    T3.join()

    
if __name__=="__main__":
    main()