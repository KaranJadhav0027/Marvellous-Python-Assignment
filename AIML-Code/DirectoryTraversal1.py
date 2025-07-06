import os

def main():
     for FolderName,SunFolderNames,FileNames in os.walk("Marvellous"):
          print("Floder name is :"+FolderName)

          for subf in SunFolderNames:
               print("Sub Folder Name is :"+subf)

          for fname in FileNames:
               print("File name is :"+fname)
   
if __name__=="__main__":
    main()