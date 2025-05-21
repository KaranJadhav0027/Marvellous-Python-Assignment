"""############################################################
  Program Accept String and check it's Palindrom or not

Input:
Enter a String :nayan

OutPut:
nayan is Pallindrom
###############################################################"""
#1st
# def CheckString(Value):
#         Data=Value
#         if Value==Data[::-1]:
#              return True
#         else:
#              return False
#2nd
# CheckString=lambda Value:Value==Value[::-1]
#3rd
def CheckString(Value):
     Data=""
     for i in Value:
          Data=i+Data
     
     if Value==Data:
          return True
     else:
          return False

def main():
    print("Enter a String :",end="")
    string=input()

    Ret=CheckString(string)
    if Ret==True:
         print(string,"is Pallindrom ")
    else:
         print(string, "is Not Pallindrom ")
         
       
if __name__=="__main__":
    main()