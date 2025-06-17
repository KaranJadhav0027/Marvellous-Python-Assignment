"""############################################################

   This code Display given Copy all files one folder to another folder

###############################################################"""

import os
import sys
import time
import shutil
import schedule

def DirectoryWatcher(DirectoryName,SecondDirectory):
    
    flag=os.path.isabs(DirectoryName) #Check the path

    if(flag ==False):
         DirectoryName=os.path.abspath(DirectoryName) #give the path (updeter)

    flag=os.path.exists(DirectoryName) #check the valid path

    if(flag==False):
         print("The path is invalid ")
         exit()
    
    flag=os.path.isdir(DirectoryName) #check its is Directory or not 
    
    if(flag==False):
         print("path is valid but the target is not a directory ")

    if not os.path.exists(SecondDirectory):
        os.mkdir(SecondDirectory)
    for FolderName,SunFolderNames,FileNames in os.walk(DirectoryName):
          for fname in FileNames:
            DFile = os.path.join(FolderName, fname)
            SFile = os.path.join(SecondDirectory, fname)
            shutil.copy(DFile,SFile) 



def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to perform Directory Cleaning")
                print("This is the Directory automation script")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py  NameOfDirectory")
                print("Please provide Valid Absolute path")

        elif(len(sys.argv)==3):
                # try:
                #     DirectoryWatcher(sys.argv[1],sys.argv[2])
                # except Exception as e:
                #     print("Give DirectryName then Extension ",e)
                schedule.every(2).seconds.do(DirectoryWatcher,sys.argv[1],sys.argv[2])

                while True:
                    schedule.run_pending()
                    time.sleep(1)

        
        else:
            print("Invalid number of Command line Arguments")
            print("Use the given flage as :")
            print("--h :Used to Display the help")
            print("--u: Used to Display the Usage")
        
        print(Border)
        print("------------Thank you for using our Script------------")
        print("----------------Marvellous Infosystems----------------")
        print(Border)


if __name__=="__main__":
    main()