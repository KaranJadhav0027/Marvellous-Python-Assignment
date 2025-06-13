"""############################################################
  
    This Program Runs Every Hour to write a BackUp File
    
###############################################################"""
import schedule
import sys
import time

def Display(FileName):
    
    timestamp=time.ctime()

    fileName="BackUp_Log.txt"

    fobj=open(fileName,"a")

    fobj.write("File BackUp :"+timestamp+".txt\n")

def main():
    
    if(len(sys.argv)==2 ):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform ---")
            print("This is the automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")
            print("ScriptName.py  Argument1 Argument2")

        else:
                FileName=sys.argv[1]
                schedule.every(1).hours.do(Display,FileName)

                while True:
                    schedule.run_pending()
                    time.sleep(1)
    else:
        print("Invalid number of Command line Arguments")
        print("Use the given flage as :")
        print("--h :Used to Display the help")
        print("--u: Used to Display the Usage")

        
if __name__=="__main__":
    main()
