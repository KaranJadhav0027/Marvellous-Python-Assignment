
class Demo:
    Value="ClassVeriable"

    def __init__(self ,No1,No2):
        self.Value1=No1
        self.Value2=No2

    def Fun(self):
        print("Inside Fun Function")
        print(self.Value1)
        print(self.Value2)
        print(self.Value)

    def Gun(self):
        print("Inside Gun Function ")
        print(self.Value1)
        print(self.Value2)
        print(self.Value)

def main():
    Obj1=Demo(11,21)
    Obj2=Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__=="__main__":
    main()