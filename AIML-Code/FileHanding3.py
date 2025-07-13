
def main():
    print("Enter the the file that you want to create :",end="")
    FileName=input()

    fobj=open(FileName,"w") 

    print("Enter the data that you want to write in the file :")
    data=input()
    
    fobj.write(data)
    fobj.close()
if __name__=="__main__":
    main()