import schedule
import time
import datetime

def MySchedule():
    print("Inside MySchedule function at :",datetime.datetime.now())

def MyScheduleX():
    print("Inside MyScheduleX function at :",datetime.datetime.now())


def main():
    print("Inside automation script ")
    print("Current time is ",datetime.datetime.now())

    # schedule.every(20).seconds.do(MySchedule)
    # schedule.every(1).minute.do(MyScheduleX)

    schedule.every(1).hour.do(MyScheduleX) 
    
    print("Application is in waiting state : ")
    
    while True:
        schedule.run_pending()
        time.sleep(1)    

if __name__=="__main__":
    main()