"""############################################################
Input:
Anika  68
Rohan  82
Priya 75
Aditya 59
Neha 90
Karan 71
Simran 64
Harshita 87
Rajan 54
Meera  79

OutPut:
Rohan  : 82
Neha  : 90
Harshita  : 87
Meera  : 79
###############################################################"""

import os
import sys

def  FileContents(FileName):

     #logic to check file 
    if os.path.exists(FileName)==True:
        Fobj=open(FileName,"r")
 
        for i in Fobj:  
            CountLine=i.strip()

            word=CountLine.split()
            if len(word)==2:
             StudentName=word[0]
             marks=int(word[1])
             if marks>75:
              print(StudentName," :",marks)


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