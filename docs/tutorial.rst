Tutorial
========


Fixed Frequency Computation
---------------------------

Cronus helps in performing certain computation at a fixed frequency, by being agnostic to the time taken by the computation.
Cronus implements a dynamic *sleep()* function to ensure a fixed loop frequency. Consider the following snippet of program. The aim is to call the function `do_some_work` at a 2 Hz frequency.

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


Forceful Timeout
----------------

Consider the following function

.. code-block:: python
    
    import time

    def dummy_computation():
        time.sleep(5)
        return "hello world"

    if __name__ == "__main__":
        reply = dummy_computation()
        print reply
        
If now, say we want to forcefully timeout the `dummy_computation` function. If this function has been implemented in some other package, we wont be able to change the source of this function. Cronus implements a `@timeout` decorator exactly for such situations!

.. code-block:: python
    
    import time
    import cronus

    @cronus.timeout(1)
    def dummy_computation():
        time.sleep(5)
        return "hello world"

    if __name__ == "__main__":
        try:
            reply = dummy_computation()
        except cronus.TimeoutError:
            print "timeout"
        else:
            print reply
