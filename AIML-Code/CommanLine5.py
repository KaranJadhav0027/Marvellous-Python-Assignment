import sys

def main():
     print("Number of CommanLine argument are :",len(sys.argv))
     print("Datatype of argv is :",type(sys.argv))

     print("List Of Command Line Argument :")

     for i in range(1,len(sys.argv)):
          print(sys.argv[i])
     
if __name__=="__main__":
      main()