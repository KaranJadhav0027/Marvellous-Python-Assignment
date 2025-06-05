class Student:
    def __init__(self,A,B,C):
        self.Name=A         #Public 
        self._Age=B         #Protected
        self.__Marks=C      #Private

    def Display(self):
        print(self.Name)  
        print(self._Age)    
        print(self.__Marks)

obj=Student("Rahul",24,89)
obj.Display()

print(obj.Name)
print(obj._Age)
#print(obj.__Marks)

