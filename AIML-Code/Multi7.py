import threading

def Display(Value1,Value2):
     print("Thread ID of child  thred is :",threading.get_ident())
     print("Inside Display ",Value1,Value2)
     for i in range(100):
         print(i)

def main():
    print("Inside main")
    print("Thread ID of main is :",threading.get_ident())
    T1=threading.Thread(target=Display,args=(11,21))
    T1.start()
    T1.join()
    print("End of main")

if __name__=="__main__":
    main()