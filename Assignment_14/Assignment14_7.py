"""############################################################

Name : Karan
Age : 21
Subject : AIML
Salary : 25000

###############################################################"""

class Person:
     def __init__(self,Name,Age):
         self.name=Name
         self.age=Age

class Teacher(Person):
    def __init__(self, Name, Age,Subject,Salary):
        super().__init__(Name, Age)
        self.subject=Subject
        self.salary=Salary

    def Display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Subject :",self.subject)
        print("Salary :",self.salary)
        
  
def main():
    Tobj=Teacher("Karan",21,"AIML",25000)
    Tobj.Display()

if __name__=="__main__":
    main()