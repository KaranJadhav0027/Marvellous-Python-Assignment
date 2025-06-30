import sys

def main():
    Border="-"*54
    print(Border)
    print("-----------------Marvellous Automation----------------")
    print(Border)
    
    if(len(sys.argv)==2 ):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform ---")
            print("This is the automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")
            print("ScriptName.py  Argument1 Argument2")

        else:
            print("Use the given flage as :")
            print("--h :Used to Display the help")
            print("--u: Used to Display the Usage")
    
    else:
        print("Invalid number of Command line Arguments")
        print("Use the given flage as :")
        print("--h :Used to Display the help")
        print("--u: Used to Display the Usage")
    
    print(Border)
    print("------------Thank you for using our Script------------")
    print("----------------Marvellous Infosystems----------------")
    print(Border)

if __name__=="__main__":
    main()