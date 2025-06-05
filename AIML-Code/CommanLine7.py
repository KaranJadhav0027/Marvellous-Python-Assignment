import sys

def Addition(No1,No2):
     Ans=0
     Ans=No1+No2
     return Ans

def main():
     if (len(sys.argv )!=3):
          print("Insufficient number of arugument ")
          return

     Value1=int(sys.argv[1])
     Value2=int(sys.argv[2])
     
     result =Addition(Value1,Value2)

     print("Addition is :",result)
     
if __name__=="__main__":
      main()