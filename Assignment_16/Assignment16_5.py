"""############################################################
------------------------------------------------------
AAAA AAAA AAAA AAAA AAAA AAAA AAAA
BBBB BBBB BBBB BBBB BBBB BB BBv BBB BBBBB vv      BBBB
EEEE  EEEE EEEE  EEEE EEEE   EEEE   EEEE
------------------------------------------------------
###############################################################"""

import os
import sys

def  FileContents(FileName):

     #logic to check file 
    if os.path.exists(FileName)==True:
        Fobj=open(FileName,"r")
 
        for i in Fobj:  
            CountLine=i.strip()
            CountWord=CountLine.strip()
            if len(CountWord)>5:
              print(CountLine)


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