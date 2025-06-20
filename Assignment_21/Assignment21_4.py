"""############################################################

This is Automation script which Display Information of running 
   processses in Give Directory 
  
 
###############################################################"""

import os
import sys
import time
import psutil
import schedule
import smtplib
import ssl
from email.message import EmailMessage

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

def ProcessDisplay(directory):
    print("*" * 25)
    print("Information of Currently Running Processess")
    print("*" * 25)

    listProcess = []
    Dir = os.path.abspath(directory)

    for proc in psutil.process_iter(['pid', 'name', 'username', 'exe']):
        try:
            exe_path = proc.info['exe']
            if exe_path and Dir in exe_path:
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

    return fileName

def SendMail(file_path,receiver_email):

    sender_email = "Mail1@gmail.com"
    sender_password = "xxxxxxxxxxxxxx"  
    subject = "Automation log mail"
    body = "Log file Send"

    try:
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        with open(file_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)

        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Email sent successfully with the log file!")

    except Exception as e:
        print(f"Error sending email: {e}")


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

        elif(len(sys.argv)==3 ):
                #  DirectoryWatcher(sys.argv[1])
                #  schedule.every(3).seconds.do(ProcessDisplay,sys.argv[1])
                #  while True:
                #    schedule.run_pending()
                #    time.sleep(1)
                directory = sys.argv[1]
                receiver_email = sys.argv[2]

                DirectoryWatcher(directory) 
                log_file = CreateLog([])  
                SendMail(log_file, receiver_email)
                
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