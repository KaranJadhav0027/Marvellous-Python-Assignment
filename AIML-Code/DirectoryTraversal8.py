import os

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

    TotalCount=0
    EmptyCount=0

    for FolderName,SunFolderNames,FileNames in os.walk(DirectoryName):
          for fname in FileNames:
               TotalCount=TotalCount+1
               if os.path.getsize(os.path.join(FolderName,fname))==0:
                  EmptyCount=EmptyCount+1
                  print("File name is :"+fname)
                  os.remove(os.path.join(FolderName,fname))

    print("Total number of Fiiles Scanned :",TotalCount)
    print("Total number of Empty file Deleted :",EmptyCount)

def main():
     
     print("Enter the name of Directory that you want to travel :")
     DirName=input()

     DirectoryWatcher(DirName)

if __name__=="__main__":
    main()