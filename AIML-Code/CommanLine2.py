import sys

def main():
     print("Number of CommanLine argument are :",len(sys.argv))
     print("Datatype of argv is :",type(sys.argv))
     print("First command line argument is :",sys.argv[0])
     print("Second command line argument is :",sys.argv[1])
     print("Third command line argument is :",sys.argv[2])
     print("Forth command line argument is :",sys.argv[3])
     
if __name__=="__main__":
      main()