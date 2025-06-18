class Base:
    def Display(self):
        print("inside Base Display")

class Derived(Base):
    def Display(self):  #overrided method
        print("inside Derived Display")

def main():
    bobj=Base()
    dobj=Derived()
    
    bobj.Display()
    dobj.Display()

if __name__=="__main__":
    main()