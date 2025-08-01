import psutil
import os
import time
import schedule

def CreateLog(FolderName):


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
    fobj.write(border+"\n")
    
    Data=ProcessScan()
    for value in Data:
        fobj.write("%s\n" %value)
        
    fobj.write(border)

    fobj.close()


def ProcessScan():

    listProcess=[]
    
    for proc in psutil.process_iter():
        try:
           info=proc.as_dict(attrs=['pid','name','username'])
           info['vms']=proc.memory_info().vms/(1024*1024)# size of memory display
           listProcess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
           pass
    return listProcess

def main():
    # Arr=ProcessScan()
    # CreateLog("MarvellousProcess",Arr)
    #cammand line crument ne kara

    schedule.every(1).minutes.do(CreateLog,"MarvellousPrecessX")

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()
