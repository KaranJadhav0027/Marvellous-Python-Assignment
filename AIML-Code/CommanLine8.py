import sys

def Addition(No1,No2):
     Ans=0
     Ans=No1+No2
     return Ans

def main():
     if(len(sys.argv)==2):
          if(sys.argv[1]=="--h"):
               print("this application is used to perform addition of 2 number")
               return
     
          if(sys.argv[1]=="--u"):
               print("Execute the code as :")
               print("python FileName.py First_Input Second_Input")
               return
     
       
     if (len(sys.argv )!=3):
          print("Insufficient number of arugument ")
          print("You can use --h for help as --u for usege")
          return

     Value1=int(sys.argv[1])
     Value2=int(sys.argv[2])
     
     result =Addition(Value1,Value2)

     print("Addition is :",result)
     
if __name__=="__main__":
      main()