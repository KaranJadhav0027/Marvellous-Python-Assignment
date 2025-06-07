"""############################################################

Inside Vehicle Strat
Insode Car start
car is Runnning

###############################################################"""

class Vehicle:
     def start(self):
         print("Inside Vehicle Strat")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Insode Car start")
   
    # def start(self):
    #     print("Insode Car start")

    def run(self):
        print("car is Runnning")     
  
def main():
   obj=Car()
   obj.start()
   obj.run()

if __name__=="__main__":
    main()