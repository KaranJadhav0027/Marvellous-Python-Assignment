"""############################################################
  Program Contain Calculate Area and Perimeter of Rectangle
  
Input:
Enter Length :5
Enter Width :3

OutPut:
Area of Rectangle : 15
Perimeter of Rectangle : 16

###############################################################"""

RectangleArea=lambda Value1,Value2 :Value1*Value2

RectanglePerimeter=lambda Value1,Value2 :(Value1+Value2)*2   
    
def main():
    print("Enter Length :",end="")
    length=int(input())

    print("Enter Width :",end="")
    width=int(input())

    Ret=RectangleArea(length,width)
    print("Area of Rectangle :",Ret)

    Ret=RectanglePerimeter(length,width)
    print("Perimeter of Rectangle :",Ret)
       

if __name__=="__main__":
    main()