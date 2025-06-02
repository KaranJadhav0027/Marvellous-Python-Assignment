"""############################################################
 Enter Redius of Cricle : 9
 
Redius of Cricle is : 9
Area of Cricle : 254.34
Circumference of Cricle : 56.52
###############################################################"""

class Circle:
    PI=3.14
    def __init__(self):
        self.Redius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter Redius of Cricle : ",end="")
        self.Redius=int(input())
    
    def CalculateArea(self):
        self.Area=self.PI*self.Redius*self.Redius

    def CalculateCircumference(self):
        self.Circumference=2*self.PI*self.Redius
    
    def Display(self):
        print("Redius of Cricle is :",self.Redius)
        print("Area of Cricle :",self.Area)
        print("Circumference of Cricle :",self.Circumference)

def main():
    obj=Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__=="__main__":
    main()