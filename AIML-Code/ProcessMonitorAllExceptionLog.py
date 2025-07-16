import psutil

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
    Arr= ProcessScan()
    for value in Arr:
        print(value)

if __name__=="__main__":
    main()
