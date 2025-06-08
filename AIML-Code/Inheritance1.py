class Circle:
    PI=3.14  #class Veriable

    def __init__(self,A):
        self.Radius=A

    def CalculateArea(self):
        Ans=0.0
        Ans=Circle.PI*self.Radius*self.Radius
        return Ans

def main():
    obj=Circle(10.5)
    Ret=obj.CalculateArea()
    print("Area of Cricle is :",Ret)

if __name__=="__main__":
    main()