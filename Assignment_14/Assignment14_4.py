"""############################################################

Name : Karan ,Roll No : 27 ,School Name : PPA

Name : Karan ,Roll No : 27 ,School Name : AIML

###############################################################"""

class Student:
    school_name="PPA"

    def __init__(self,name,Roll_no):
        self.Name=name
        self.roll_no=Roll_no

    def Display(self):
        print("Name :",self.Name,",Roll No :",self.roll_no,",School Name :",self.school_name)


def main():
    sobj=Student("Karan",27)

    sobj.Display()

    sobj.school_name="AIML"
    sobj.Display()

if __name__=="__main__":
    main()