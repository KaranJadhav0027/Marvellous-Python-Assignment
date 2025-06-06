"""############################################################

Linux Systen Programming  By  Robert Love No of Book : 1

C Programming  By  Dennis Ritchi No of Book : 2

###############################################################"""

class BookStore:
    NoOfBooks=0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
    
    def Display(self):
       
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
        print(self.Name," By ",self.Author,"No of Book :",BookStore.NoOfBooks)
        

def main():
    Bobj=BookStore("Linux Systen Programming","Robert Love")
    Bobj.Display()

    Bobj2=BookStore("C Programming","Dennis Ritchi")
    Bobj2.Display()

if __name__=="__main__":
    main()