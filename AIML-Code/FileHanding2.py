

def main():
    print("Enter the the file that you want to create :",end="")
    FileName=input()

    fobj=open(FileName,"x") #aset tr error deil nasel tr create karel

    fobj.close()
if __name__=="__main__":
    main()