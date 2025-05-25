"""############################################################
  program creating two thread which Display 1 to 50 and 50 to 1 number

###############################################################"""
import threading

def thread1():
    for i in range(51):
      print("Thread1 :",i)

def thread2():
     for i in range(50,0,-1):
       print("Thread2 :",i)
                 
        
def main():
    
    T1=threading.Thread(target=thread1)
    T2=threading.Thread(target=thread2)
    T1.start()
    T1.join() 
    #After the end the 1st Thread then start 2nd thread
    T2.start()
    T2.join()
    
if __name__=="__main__":
    main()