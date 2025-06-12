"""############################################################
Input:
AIML-Assignement>python Assignment16_3.py  Student.txt

Output:
------------------------------------------------------
-----------------Marvellous Automation----------------
------------------------------------------------------
Student.txt having  5 of Word
Student.txt having  24 of characters
Student.txt having  5 of Lions
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
        Fobj=open(FileName,"r")
        Data=Fobj.read()
        CounWord=len(Data.split())
        CountChar=len(Data)

        NumberLine=Data.count('\n')
        if Data:
            CountLine=NumberLine+1
        else:
            CountLine=0
            
        print(FileName,"having ",CounWord,"of Word ")
        print(FileName,"having ",CountChar,"of characters ")
        print(FileName,"having ",CountLine,"of Lions ")

        Fobj.close() 

    else:
        print (FileName,"is not exit")
   
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