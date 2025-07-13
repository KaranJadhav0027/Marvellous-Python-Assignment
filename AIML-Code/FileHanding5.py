import os

def main():
    print("Enter the the file that you want to read :",end="")
    FileName=input()
   
    ret=os.path.exists(FileName)

    if(ret==True):
        print("File is present in the current diractory ")
        fobj=open(FileName,"r")
        data=fobj.read()  # for all data in file 
        # data=fobj.read(5)  #

        print("Data from File is :",data)

        fobj.close()
    else:
        print("There is no such File")

if __name__=="__main__":
    main()