import os

def main():
    print("Enter the the file that you want to check :",end="")
    FileName=input()
   
    ret=os.path.exists(FileName)

    if(ret==True):
        print("File is present in the current diractory ")
    else:
        print("There is no such File")

if __name__=="__main__":
    main()