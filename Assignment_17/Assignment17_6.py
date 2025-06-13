"""############################################################

    This program display "Lunch Time " in 1 PM
    and Display "Wrap up Work " in 6 PM

###############################################################"""
import schedule
import time

def Lunch():
    print("Lunch Time !")

def Wrap():
    print("Wrap up work ")

def main():
    schedule.every().day.at("13:00").do(Lunch)  
    schedule.every().day.at("18:00").do(Wrap) 

    while True:
        schedule.run_pending()
        time.sleep(1) 

if __name__=="__main__":
    main()

