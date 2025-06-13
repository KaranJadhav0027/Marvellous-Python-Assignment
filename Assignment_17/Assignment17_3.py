"""############################################################

    This program display "Do Coding....!" in every 30 Minute

###############################################################"""
import schedule
import time

def Displays():
    print("Do Coding....!")

def main():
    schedule.every(30).minutes.do(Displays)

    while True:
        schedule.run_pending()
        time.sleep(1) 

if __name__=="__main__":
    main()

