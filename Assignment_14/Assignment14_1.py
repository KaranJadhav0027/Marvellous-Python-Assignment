"""############################################################

Name : Rohil ,ID : 101 ,Salary : 50000

###############################################################"""


class Employee:
    def __init__(self,name,Emp_id,Salary):
        self.Name=name
        self.emp_id=Emp_id
        self.salary=Salary

    def Display(self):
        print("Name :",self.Name,",ID :",self.emp_id,",Salary :",self.salary)


def main():
    eobj=Employee("Rohil",101,50000)
    eobj.Display()

if __name__=="__main__":
    main()