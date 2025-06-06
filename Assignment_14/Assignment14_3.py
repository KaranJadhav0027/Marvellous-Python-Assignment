"""############################################################

price of Book : 400

price after set Book : 200

###############################################################"""

class Book:
    def __init__(self,Price):
        self.__price=Price

    def get(self):
        return self.__price
    
    def set(self,NPrice):
        self.__price=NPrice
        return self.__price   

def main():
    bobj=Book(400)
    Ret=bobj.get()
    print("price of Book :",Ret)

    Ret=bobj.set(200)
    print("price after set Book :",Ret)

if __name__=="__main__":
    main()