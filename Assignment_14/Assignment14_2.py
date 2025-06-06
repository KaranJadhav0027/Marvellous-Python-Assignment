"""############################################################

Area of Rectangle : 110

Perimeter of Rectangle : 42

###############################################################"""

class Rectangle:
    def __init__(self,Length,Width):
        self.length=Length
        self.width=Width

    def RetArea(self):
        area=self.width*self.length
        return area
    
    def RetPerimeter(self):
        perimeter=2*(self.width+self.length)
        return perimeter

def main():
    Robj=Rectangle(11,10)
    ARet=Robj.RetArea()
    PRet=Robj.RetPerimeter()

    print("Area of Rectangle :",ARet)
    print("Perimeter of Rectangle :",PRet)


if __name__=="__main__":
    main()