import cronus
import time
import datetime

def do_some_work():
    time.sleep(0.3)
    pass

if __name__ == "__main__":
    cronus.set_rate(2)
    while cronus.true():
        do_some_work()
        cronus.sleep()
        print datetime.datetime.now()

