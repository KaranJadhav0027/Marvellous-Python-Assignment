"""############################################################

Input:
AIML-Assignement>python Assignment18_3.py demo.txt demo2.txt
Output:
------------------------------------------------------
Copy All content from existing file to new file
------------------------------------------------------

Input:
AIML-Assignement>python Assignment15_3.py demo.txt demo2.txt

------------------------------------------------------
demo2.txt  is already exit
------------------------------------------------------

Input:
AIML-Assignement>python Assignment15_3.py demo3.txt demo2.txt

Output:
------------------------------------------------------
demo3.txt is not exit
------------------------------------------------------

###############################################################"""

import os
import sys

def  FileContents(FileName, CopyName):

     #logic to check file 
    if os.path.exists(FileName)==True  and os.path.exists(CopyName)==False:
        Nobj=open(FileName,"r")
        Cobj=open(CopyName,"w")
        data=Nobj.read()
        Cobj.write(data)
        print("Copy All content from existing file to new file ")
    
        Cobj.close()
        Nobj.close()

    else:
        if os.path.exists(FileName)==False:
          print (FileName,"is not exit")
        else :
            print(CopyName," is already exit")
   
def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==3 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to Display the Content one file  data copy in another  file\n")
               
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