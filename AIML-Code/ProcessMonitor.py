import psutil

def ProcessDisplay():
    Border="*"*25
    print(Border)
    print("Information of Currently Running Processess")
    print(Border)

    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=['pid','name'])
        print(info)

def main():
    ProcessDisplay()

if __name__=="__main__":
    main()
