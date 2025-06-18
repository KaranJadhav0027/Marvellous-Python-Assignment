class Employee:
    CompanyName="Marvellous"  # Class Veriable: its lick a static Variable
    
    def __init__(self,A,B,C):   # Constructor
        print("Inside Constructor")
        self.Name=A           #Instance Variable
        self.Salary=B         #Instance Variable
        self.City=C           #Instance Variable
    
    def __del__(self):          # Destructor
        print("Inside Destructor")

    def DisplayInfo(self):           #Instance Method  (it Also featch all methos)
        print("Inside Instance Method DisplayInfo :")
        print("Emplyee Name :"+self.Name)
        print("Emplyee Salary :",self.Salary)
        print("Emplyee City :"+self.City)
   
    @classmethod   #Decorater 
    def DisplayCompanyDetails(cls): #Class Method
        print("Inside class Method DisplayCompanyDetails :")
        print("Company Name :"+cls.CompanyName)
    
    @staticmethod  #Decorater
    def DisplayCompanyPolicy():
        print("Inside Static Method DisplayCompanyPolicy :")
        print("All Employees are 18+")
        print("Working hours are 9 to 6")
        print("Holiday : Saturday & Sunday")

def main():
   print("Class Variable : "+Employee.CompanyName)
   Employee.DisplayCompanyDetails()

   emp1=Employee('Rahul',15000,'Pune')   # Object Creation
   emp2=Employee('Pooja',25000,'Nashik')  #object Creation

   print("Emplyee Name :"+emp1.Name)   #instance Veriable Access
   print("Emplyee Salary :",emp1.Salary)
   print("Emplyee City :"+emp1.City)

   emp2.DisplayInfo()

   Employee.DisplayCompanyPolicy()

   del emp1
   del emp2
if __name__=="__main__":
    main()