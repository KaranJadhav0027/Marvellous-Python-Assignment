

def main():
    print("Enter the the file that you want to create :",end="")
    FileName=input()

    fobj=open(FileName,"w") #banavel asel tr ti used karayala deil
    
    fobj.close()
    
if __name__=="__main__":
    main()