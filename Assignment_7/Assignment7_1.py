"""############################################################
  Program Accept number And Display Square and Cube

Input:
Enter a Number :3

Output:
Square of : 9
Square of : 27
###############################################################"""

Square=lambda SValue:SValue*SValue
Cube=lambda CValue:CValue**3

def main():
    print("Enter a Number :",end="")
    No=int(input())

    Ret=Square(No)
    print("Square of :",Ret)

    Ret=Cube(No)
    print("Square of :",Ret)

if __name__=="__main__":
    main()