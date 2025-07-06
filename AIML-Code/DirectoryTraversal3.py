import os

def DirectoryWatcher(DirectoryName):
   
    for FolderName,SunFolderNames,FileNames in os.walk(DirectoryName):
          print("Floder name is :"+FolderName)

          for subf in SunFolderNames:
               print("Sub Folder Name is :"+subf)

          for fname in FileNames:
               print("File name is :"+fname)
   
     
def main():
     
     print("Enter the name of Directory that you want to travel :")
     DirName=input()

     DirectoryWatcher(DirName)

if __name__=="__main__":
    main()