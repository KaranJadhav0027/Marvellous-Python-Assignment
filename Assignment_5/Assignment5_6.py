"""############################################################
  Program Contain Converter in Celsius to Fahrenheit
  
Input:
Enter temperature in celsius :25

OutPut:
Temperature in  Fahrenheit : 77.0 F

###############################################################"""

# def Converter(Value):
#     Fhr=0
#     Fhr=(Value*(9/5))+32
#     return Fhr

Converter=lambda Value:(Value*(9/5))+32
    
def main():
    print("Enter temperature in celsius :",end="")
    No=int(input())

    Ret=Converter(No)
    print("Temperature in  Fahrenheit :",Ret,"F")
       

if __name__=="__main__":
    main()