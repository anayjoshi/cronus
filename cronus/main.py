import cronus
import time
import datetime

if __name__ == "__main__":
    cronus.set_rate(2)
    while cronus.true():
        print datetime.datetime.now()
        time.sleep(1)
        cronus.sleep()

