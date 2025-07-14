import sys
import time

def Createlog():
        timestamp=time.ctime()

        fileName="MarvellousLog %s.log" %(timestamp)
        
        fileName=fileName.replace(" ","_")
        fileName=fileName.replace(":","_")

        fobj=open(fileName,"w")
        
        Border="-"*54
        fobj.write(Border+"\n")
        fobj.write("This is a log file of Marvellous Automation Script\n")
        fobj.write(Border+"\n")

        fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        fobj.write(Border+"\n")
        fobj.write("File created at :\n"+timestamp+"\n")
        fobj.write(Border+"\n")

def main():
      Createlog()
   
if __name__=="__main__":
    main()