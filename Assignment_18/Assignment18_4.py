"""############################################################

Input:
\AIML-Assignement>python Assignment18_4.py Demo.py Student.txt

Output:
------------------------------------------------------
-----------------Marvellous Automation----------------
------------------------------------------------------
Data in File is Same :
Data in File is : ABCDEFGHIJKLMNOPQRSTUVWXYZ
------------------------------------------------------
------------Thank you for using our Application-------
----------------Marvellous Infosystems----------------
------------------------------------------------------
###############################################################"""

import os
import sys
import hashlib

def CalculateCheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()

    buffer=fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def  FileContents(FirstFile, SecondFile):

     #logic to check file 
    if os.path.exists(FirstFile)==True  and os.path.exists(SecondFile)==True:
        CheckFirstdata=CalculateCheckSum(FirstFile)
        CheckSeconddata=CalculateCheckSum(SecondFile)
        Fobj=open(FirstFile,"r")
        Sobj=open(SecondFile,"r")
        Fdata=Fobj.read()
        Sdata=Sobj.read()
        if CheckFirstdata==CheckSeconddata:
           
            print("Data in File is Same :")
            print("Data in File is :",Fdata)
        else:
            print("Data in both files are Different")
            print(" Data in First File \n",Fdata)
            print(" Data in Secoond File \n",Sdata)

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