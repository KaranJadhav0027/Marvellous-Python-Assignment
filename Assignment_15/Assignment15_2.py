"""############################################################
Input:
python Assignment15_1.py Arithematic.py

Output:
------------------------------------------------------
-----------------Marvellous Automation----------------
------------------------------------------------------
Data from File is : def Add(Value1,Value2):
    return Value1+Value2

def Sub(Value1,Value2):
    return Value1-Value2

def Mult(Value1,Value2):
    return Value1*Value2

def Div(Value1,Value2):
    if Value2==0:
        print("Enter Greater than Zero Value")
    return Value1/Value2

------------------------------------------------------
------------Thank you for using our Application-------
----------------Marvellous Infosystems----------------
------------------------------------------------------

###############################################################"""

import os
import sys

def  FileContents(FileName):

     #logic to check file 
    if os.path.exists(FileName)==True:
        fobj=open(FileName,"r")
        data=fobj.read()  

        print("Data from File is :",data)

        fobj.close()
        
    else:
        print (FileName,"is not exit")
   
def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to Display the Contents of that file\n")
               
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py  NameOfDirectory")
                print("Please provide Valid Absolute path")

            else:
                FileContents(sys.argv[1])
        
        else:
            print("Invalid number of Command line Arguments")
            print("Use the given flage as :")
            print("--h :Used to Display the help")
            print("--u: Used to Display the Usage")
        
        print(Border)
        print("------------Thank you for using our Application-------")
        print("----------------Marvellous Infosystems----------------")
        print(Border)


if __name__=="__main__":
    main()