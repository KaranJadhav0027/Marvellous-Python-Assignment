import threading

def Display(Value1,Value2):
     print("Inside Display ",Value1,Value2)
     for i in range(100):
         print(i)

def main():
    print("Inside main")
    T1=threading.Thread(target=Display,args=(11,21))
    T1.start()
    print("End of main")

if __name__=="__main__":
    main()