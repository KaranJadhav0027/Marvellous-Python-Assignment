"""############################################################

1st and 2nd Object : True

2nd and 3rd Object : False

1st and 3rd Object : False

###############################################################"""

class Product:
    def __init__(self,name,price):
        self.Name=name
        self.Price=price

    def __eq__(self,Compare):
        if self.Name==Compare.Name and self.Price==Compare.Price:
            return True
        else:
            return False
         
def main():
    obj1=Product("xyz",1000)
    obj2=Product("xyz",1000)
    obj3=Product("ABC",3000)
 
    print("1st and 2nd Object :",obj1==obj2)
    print("2nd and 3rd Object :",obj2==obj3)
    print("1st and 3rd Object :",obj1==obj3)

if __name__=="__main__":
    main()