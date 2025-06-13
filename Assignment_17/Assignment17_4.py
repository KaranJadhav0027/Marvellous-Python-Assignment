"""############################################################

    This program display "Namskar...." in every Day 9:00 AM

###############################################################"""
import schedule
import time

def Displays():
    print("Namskar....")

def main():
    schedule.every(30).day.at("09:00").do(Displays)

    while True:
        schedule.run_pending()
        time.sleep(1) 

if __name__=="__main__":
    main()

