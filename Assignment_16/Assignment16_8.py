"""############################################################

Input:
AIML-Assignement>python Assignment16_8.py  Student.txt demo.txt

OutPut:
------------------------------------------------------
-----------------Marvellous Automation----------------
------------------------------------------------------
Copy All content from existing file to new file
------------------------------------------------------
------------Thank you for using our Application-------
----------------Marvellous Infosystems----------------
------------------------------------------------------
###############################################################"""

import os
import sys

def  FileContents(Source, Destination):

     #logic to check file 
    if os.path.exists(Source)==True  and os.path.exists(Destination)==False:
        Sobj=open(Source,"r")
        Dobj=open(Destination,"w")
        for i in Sobj:
            if i.strip():
             Dobj.write(i)
        print("Copy All content from existing file to new file ")
    
        Sobj.close()
        Dobj.close()

    else:
        if os.path.exists(Source)==False:
          print (Source,"is not exit")
        else :
            print(Destination," is already exit")
   
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