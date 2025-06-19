"""############################################################

   This is Automation script which Display Information of running 
   processses in Log File 

###############################################################"""
import os
import sys
import time
import psutil
import schedule

def ProcessDisplay():
    Border="*"*25
    print(Border)
    print("Information of Currently Running Processess")
    print(Border)
    
    listProcess=[]
    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=['pid','name','username'])
            info['vms']=proc.memory_info().vms/(1024*1024)# size of memory display
            listProcess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
           pass
    CreateLog(listProcess)


def CreateLog(Data,FolderName="Marvellous"):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    
    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    timestamp=timestamp.replace("/","_")

    FileName=os.path.join(FolderName,"Marvellous%s.log" %(timestamp))
    
    fobj=open(FileName,"w")

    border="-"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosysten process Log \n")
    fobj.write("\t\tLog File is Created at :"+time.ctime()+"\n")
    fobj.write(border)
    
    for value in Data:
        fobj.write("%s \n" %value)
        
    fobj.write(border)

    fobj.close()


def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)

        if(len(sys.argv)==1):
            # ProcessDisplay()
            schedule.every(3).seconds.do(ProcessDisplay)
            while True:
                schedule.run_pending()
                time.sleep(1)
        
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to perform Display NAme of Process")
                print("This is the Process automation script")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py ")

              
            else:
                print("Invalid number of Command line Arguments")
                print("Use the given flage as :")
                print("--h :Used to Display the help")
                print("--u: Used to Display the Usage")
            
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