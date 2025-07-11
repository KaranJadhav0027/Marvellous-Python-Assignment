import os

def main():
    print("Enter the name of Directory ")
    DirName=input()

    ret=os.path.isabs(DirName)

    if(ret==True):
        print("Input is absulute path")
    else:
        print("Input is relative path")

if __name__=="__main__":
    main()

#Absulute path
#C:\Users\jadha\OneDrive\Desktop\Home\AIML\Automations\Marvellous\AI

#relative path
#Home\AIML\Automations\Marvellous\AI