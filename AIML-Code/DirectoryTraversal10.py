import os
import sys
import time

def DirectoryWatcher(DirectoryName="Marvellous"):
    
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

    
    print("Absolute path is : "+DirectoryName)

    TotalCount=0
    EmptyCount=0

    for FolderName,SunFolderNames,FileNames in os.walk(DirectoryName):
          for fname in FileNames:
               TotalCount=TotalCount+1
               if os.path.getsize(os.path.join(FolderName,fname))==0:
                  EmptyCount=EmptyCount+1
                  print("File name is :"+fname)
                  os.remove(os.path.join(FolderName,fname))

    
    
    timestamp=time.ctime()

    fileName="MarvellousLog %s.log" %(timestamp)
    
    fileName=fileName.replace(" ","_")
    fileName=fileName.replace(":","_")

    fobj=open(fileName,"w")
    
    Border="-"*54
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectrory cleaner Script")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n")
    fobj.write("Total number of Fiiles Scanned :"+str(TotalCount)+"\n")
    fobj.write("Total number of Empty file Deleted :"+str(EmptyCount)+"\n")
    fobj.write("\n\n\n\n\n")
    
    fobj.write(Border+"\n")
    fobj.write("File created at :\n"+timestamp+"\n")
    fobj.write(Border+"\n")
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

            else:
                DirectoryWatcher(sys.argv[1])
        
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