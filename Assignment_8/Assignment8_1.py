"""############################################################
  program creating two thread which Display First 10 odd And Even Number

OutPut:
2
4
6
1
3
5
7
9
11
13
8
10
12
14
16
18
20
15
17
19

###############################################################"""

import threading

def Even():
    for i in range(2,21,2):
            print(i)

def Odd():
    for i in range(1,21,2):
            print(i)
        
def main():
    
    T1=threading.Thread(target=Even)
    T2=threading.Thread(target=Odd)
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__=="__main__":
    main()