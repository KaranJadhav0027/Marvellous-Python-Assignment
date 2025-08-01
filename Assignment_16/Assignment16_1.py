"""############################################################
Input:
AIML-Assignement>python Assignment16_1.py  Student.txt

------------------------------------------------------
-----------------Marvellous Automation----------------
------------------------------------------------------
Enter the 5 Student Name:
AAAA
BBBB
CCCC
DDDD
EEEE

Student Names Added successfully
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
         print(FileName,"is Exit Give Another name")         
         return

    Fobj=open(FileName,"w")
    SData=[]
    print("Enter the 5 Student Name:")
    for i in range(5):
        Name=input()
        SData.append(Name)
    Fobj.write("\n".join(SData))

    print("Student Names Added successfully")
    Fobj.close() 

def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to Display the Content one file  data copy in another  file\n")
               
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py  NameFile  CopyFile")
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