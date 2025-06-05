
def main():
    Ans=0
    try:
        print("Enter First number :",end="")
        No1=int(input())

        print("Enter Second number :",end="")
        No2=int(input())
        
        Ans=No1/No2

    except ZeroDivisionError as zobj:
        print("Exception occured due to Second Input :",zobj)

    except ValueError as vobj:
        print("Invalid Data type of  input :",vobj)
        
    print("Division is :",Ans)
    
if __name__=="__main__":
    main()