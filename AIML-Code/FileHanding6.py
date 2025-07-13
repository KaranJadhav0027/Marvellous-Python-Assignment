import os

def main():
    print("Enter the the file that you want to delete :",end="")
    FileName=input()
   
    ret=os.path.exists(FileName)

    if(ret==True):
        print("File is present in the current diractory ")
        
        os.remove(FileName)

    else:
        print("There is no such File")

if __name__=="__main__":
    main()