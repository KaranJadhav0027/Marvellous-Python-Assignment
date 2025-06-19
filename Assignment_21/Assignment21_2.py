"""############################################################

   This is Automation script which Display Information of running 
   processses in Log File 

 Process Name      : Notepad.exe
Process ID        : 17540
Parent Process ID : 3612
Status            : running
CPU Percent       : 0.0 %
 
###############################################################"""
import os
import sys
import time
import psutil
import schedule

def ProcessInfo(pid):
    #template copy from crome
    try:
        process = psutil.Process(pid)
        info = []

        info.append("Process Name      : " + str(process.name()))
        info.append("Process ID        : " + str(process.pid))
        info.append("Parent Process ID : " + str(process.ppid()))
        info.append("Status            : " + str(process.status()))
        info.append("CPU Percent       : " + str(process.cpu_percent(interval=1.0)) + " %")
        info.append("Memory Info       : " + str(process.memory_info()))
        info.append("Number of Threads : " + str(process.num_threads()))
        info.append("Executable Path   : " + str(process.exe()))
         
        info.extend(info)
        info.append("-" * 80)  # Add separator between processes
        CreateLog(info)

    except psutil.NoSuchProcess:
        print(f"No process found with PID: {pid}")
    except psutil.AccessDenied:
        print(f"Access denied to process with PID: {pid}")


def ProcessDisplay(ProcessName):
    Border="*"*25
    print(Border)
    print("Information of Currently Running Processess")
    print(Border)
   
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == ProcessName:
                found = True
                ProcessInfo(proc.info['pid'])
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not found:
        print(f"No process named '{ProcessName}' found.")
    
    
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
    
    for line in Data:
            fobj.write(line + "\n")
        
    fobj.write(border)

    fobj.close()


def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
       
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to perform Display NAme of Process")
                print("This is the Process automation script")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py ")

              
            else:
                # ProcessDisplay(sys.argv[1])
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