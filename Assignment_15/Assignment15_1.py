"""############################################################
Input:
python Assignment15_1.py Assignment14_1.py

Output:
------------------------------------------------------
-----------------Marvellous Automation----------------
------------------------------------------------------
Assignment14_1.py is Exit
------------------------------------------------------
------------Thank you for using our Application-------
----------------Marvellous Infosystems----------------
------------------------------------------------------


###############################################################"""

import os
import sys

def  FileExist(FileName):

     #logic to check file 
    if os.path.exists(FileName)==True:
        print(FileName,"is Exit")
    else:
        print (FileName,"is not exit")
   
def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to perform to check Exists File\n")
               
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py  NameOfDirectory")
                print("Please provide Valid Absolute path")

            else:
                FileExist(sys.argv[1])
        
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