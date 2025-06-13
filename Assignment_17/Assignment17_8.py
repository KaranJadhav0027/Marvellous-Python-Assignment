"""############################################################

    This program check mail  in every 10 Seconds

###############################################################"""
import schedule
import time
import random

def mailCheck():
    mail=random.choice([True,False])
    if mail==True:
        print("New Email ")
    else:
        print("Not New Email ")
def main():
    schedule.every(10).seconds.do(mailCheck)

    while True:
        schedule.run_pending()
        time.sleep(1) 

if __name__=="__main__":
    main()

