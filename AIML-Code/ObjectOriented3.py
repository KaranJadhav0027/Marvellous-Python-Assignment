class Employee:
    CompanyName="Marvellous"  # Class Veriable: its lick a static Variable
    
    def __init__(self,A,B,C):
        print("Inside Constructor")
        self.Name=A
        self.Salary=B
        self.City=C
    
    def __del__(self):
        print("Inside Destructor")

def main():
   print("Class Variable : "+Employee.CompanyName)

   emp1=Employee('Rahul',15000,'Pune')
   emp2=Employee('Pooja',25000,'Nashik')

   print("Emplyee Name :"+emp1.Name)
   print("Emplyee Salary :",emp1.Salary)
   print("Emplyee City :"+emp1.City)

if __name__=="__main__":
    main()