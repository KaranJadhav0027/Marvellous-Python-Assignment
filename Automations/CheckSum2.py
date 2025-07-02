import os
import hashlib

def CalculateCheckSum(path):
    fobj=open(path,"rb")

    hobj=hashlib.md5()

    buffer=fobj.read(100)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(100)

    fobj.close()

    return hobj.hexdigest()


def main():
    print("Enter File name")
    filename=input()

    Ret=CalculateCheckSum(filename)

    print("CheckSum of file is :",Ret)
      
if __name__=="__main__":
    main()