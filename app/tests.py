import schedule
import time

def its_time():
    print("Doing the joob")


while True:
    schedule.run_pending()
    time.sleep(1)
    print("I am running")