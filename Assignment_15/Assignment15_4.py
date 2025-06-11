"""############################################################

Input:
\AIML-Assignement>python Assignment15_4.py demo.txt demo2.txt

Output:
------------------------------------------------------
Data in File is : ABCDEFGHIJKLMNOPQRSTUVWXYZ
------------------------------------------------------

###############################################################"""

import os
import sys

def  FileContents(FirstFile, SecondFile):

     #logic to check file 
    if os.path.exists(FirstFile)==True  and os.path.exists(SecondFile)==True:
        Fobj=open(FirstFile,"r")
        Sobj=open(SecondFile,"r")
        Fdata=Fobj.read()
        Sdata=Sobj.read()
        if Fdata==Sdata:
            print("Data in File is :",Fdata)
        else:
            print("Data are not same in both files ")
        
        Fobj.close()
        Sobj.close()
    else:
        if os.path.exists(FirstFile)==False:
          print (FirstFile,"is not exit")
        elif os.path.exists(SecondFile)==False:
            print(SecondFile,"is not exit")
        
def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==3 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to Display the Content one file to Compare another  file\n")
               
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py  NameFile  CopyFile")
                print("Please provide Valid Absolute path")

            else:
                FileContents(sys.argv[1],sys.argv[2])
        
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