"""############################################################

This Automation script Accept Directory name and Delete 
  the all Duplicate files and Display the Execution time 

###############################################################"""

import os
import sys
import time
import hashlib
import schedule

def CalculateCheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()

    buffer=fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

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

    Files={}
    for FolderName,SunFolderNames,FileNames in os.walk(DirectoryName):
          for fname in FileNames:
             fname=os.path.join(FolderName,fname) 
             checksum=CalculateCheckSum(fname) 
             if checksum in Files:
               Files[checksum].append(fname)
             else:
               Files[checksum] = [fname]
    return Files

def DeleteDuplicate(Path="Marvellous"):
     StartTime=time.time()
     MyDict=DirectoryWatcher(Path)
     Result=list(filter(lambda x:len(x)>1,MyDict.values()))
     Count=0
     Cnt=0
     Files=[]
     
     for value in Result:
          for subvalue in value:
               Count=Count+1
               if(Count>1):
                    # print("Deleted file :",subvalue)
                    Files.append(subvalue)
                    os.remove(subvalue) 
                    Cnt=Cnt+1     
          Count=0
     CreateLog(Files)
     EndTime=time.time()
     print("Total Execution time is :",EndTime-StartTime)

     print("Total Deleted File :",Cnt)
    
def CreateLog(Files):
    Dir="Demo"
    if not os.path.exists(Dir):
          os.makedirs(Dir)
    timestamp=time.ctime()

    fileName=os.path.join(Dir,"MarvellousLog %s.log" %(timestamp))
    
    fileName=fileName.replace(" ","_")
    fileName=fileName.replace(":","_")

    fobj=open(fileName,"w")
    
    Border="-"*54
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectrory cleaner Script")
    fobj.write(Border+"\n")
    
    for F in Files:
          fobj.write(F+"\n")
    
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
                schedule.every(3).seconds.do(DeleteDuplicate,sys.argv[1])

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