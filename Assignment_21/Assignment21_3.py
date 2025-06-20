"""############################################################

This is Automation script which Display Information of running 
   processses in Give Directory 
  
 
###############################################################"""

import os
import sys
import time
import psutil
import schedule

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

    for FolderName,SubFolderNames,FileNames in os.walk(DirectoryName):
          for fname in FileNames:
               pass
    ProcessDisplay(DirectoryName)


# def ProcessDisplay():
#     Border="*"*25
#     print(Border)
#     print("Information of Currently Running Processess")
#     print(Border)
    
#     listProcess=[]
#     for proc in psutil.process_iter():
#         try:
#             info=proc.as_dict(attrs=['pid','name','username'])
#             info['vms']=proc.memory_info().vms/(1024*1024)# size of memory display
#             listProcess.append(info)
#         except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
#            pass
#     CreateLog(listProcess)
def ProcessDisplay(directory):
    print("*" * 25)
    print("Information of Currently Running Processess")
    print("*" * 25)

    listProcess = []
    Dir = os.path.abspath(directory)

    for proc in psutil.process_iter(['pid', 'name', 'username', 'exe']):
        try:
            exe_path = proc.info['exe']
            if exe_path and exe_path.startswith(Dir):
                info = {
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'username': proc.info['username'],
                     'vms': proc.memory_info().vms / (1024 * 1024)
                }
                listProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

        CreateLog(listProcess)
     

def CreateLog(Data):
    Dir="Marvellous"
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
    
    for value in Data:
        fobj.write("%s \n" %value)
    
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
                # DirectoryWatcher(sys.argv[1])
                 schedule.every(3).seconds.do(ProcessDisplay,sys.argv[1])
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
