"""############################################################

Inside Employee Class

Public Name : karan
Proctected Department : IT
Private Salary : 25000

CAll in main

Public Name : karan
Proctected Department : IT

###############################################################"""

class Employee:
     def __init__(self, name, department, salary):
        self.name = name              
        self._department = department 
        self.__salary = salary 
   
     def Display(self):
         print("Inside Employee Class ")
         print("Public Name :",self.name)
         print("Proctected Department :",self._department)
         print("Private Salary :",self.__salary)
      
def main():
    obj=Employee("karan","IT",25000)
    obj.Display()

    print("CAll in main ")
    print("Public Name :",obj.name)
    print("Proctected Department :",obj._department)
    # print("private Salary :",obj.__salary)  # private are not access in out of Employee class   


if __name__=="__main__":
    main()