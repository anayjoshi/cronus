Tutorial
========

Consider the following snippet of program. The aim is to call the function `do_some_work` at a 2 Hz frequency.

.. code-block:: python

    import time
    import datetime

    def do_some_work():
        # sleep simulates some work
        time.sleep(0.3)

    if __name__ == "__main__":
        while True:
            do_some_work()
            time.sleep(0.5)
            print datetime.datetime.now()

Unfortunately, the above methodology does not take into account the time taken by the function `do_some_work`. Cronus is meant to solve the above mentioned problem.


.. code-block:: python

    import cronus
    import time
    import datetime

    def do_some_work():
        time.sleep(0.3)

    if __name__ == "__main__":
        # specify rate in Hz
        cronus.set_rate(2)
        while cronus.true():
            do_some_work()
            cronus.sleep()
            print datetime.datetime.now()


