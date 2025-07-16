import psutil

def ProcessDisplay():
    Border="*"*25
    print(Border)
    print("Information of Currently Running Processess")
    print(Border)

    for proc in psutil.process_iter():
        try:
           info=proc.as_dict(attrs=['pid','name','username'])
           info['vms']=proc.memory_info().vms/(1024*1024)# size of memory display
           print(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
           pass

def main():
    ProcessDisplay()

if __name__=="__main__":
    main()
