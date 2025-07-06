import os

def DirectoryWatcher():
    for FolderName,SunFolderNames,FileNames in os.walk("Marvellous"):
          print("Floder name is :"+FolderName)

          for subf in SunFolderNames:
               print("Sub Folder Name is :"+subf)

          for fname in FileNames:
               print("File name is :"+fname)
   
     
def main():
     DirectoryWatcher()

if __name__=="__main__":
    main()