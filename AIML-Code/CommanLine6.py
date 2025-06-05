def Addition(No1,No2):
     Ans=0
     Ans=No1+No2
     return Ans

def main():
     Value1=int(input("Enter First Number  :"))
     Value2=int(input("Enter Second Number  :"))

     result =Addition(Value1,Value2)

     print("Addition is :",result)
     
if __name__=="__main__":
      main()