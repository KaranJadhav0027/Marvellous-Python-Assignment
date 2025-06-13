"""############################################################

    This program display Date and time  in every 1 Minute

###############################################################"""
import schedule
import time
import datetime

def Displays():
    print("Current Data and Time :",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(Displays)

    while True:
        schedule.run_pending()
        time.sleep(1) 

if __name__=="__main__":
    main()

