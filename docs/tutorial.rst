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

Unfortunately, the above methodology does not take into account the time taken by the function `do_some_work`. Cronus helps us solve this.


.. code-block:: python

    import cronus.beat as beat
    import time
    import datetime

    def do_some_work():
        time.sleep(0.3)

    if __name__ == "__main__":
        # specify rate in Hz
        beat.set_rate(2)
        while beat.true():
            do_some_work()
            beat.sleep()
            print datetime.datetime.now()


Forceful Timeout
----------------

Several times, I wanted to forcefully timeout some function which relies on third party functions, as the third party functions just don't timeout as they promise!

.. code-block:: python

    import time

    def third_party_function():
        time.sleep(5)
        return "hello world"

    if __name__ == "__main__":
        reply = third_party_function()
        print reply

If now, say we want to forcefully timeout the `third_party_function` function. If this function has been implemented in some other package, we wont be able to change the source of this function. Cronus implements a `@timeout` decorator exactly for such situations!

.. code-block:: python

    import time
    from cronus.timeout import timeout, TimeoutError

    @timeout(1)
    def third_party_function():
        time.sleep(5)
        return "hello world"

    if __name__ == "__main__":
        try:
            reply = third_party_function()
        except TimeoutError:
            print "timeout"
        else:
            print reply

Try reducing the sleep duration in `third_party_function` to say, 0.5 seconds. Things would work as you expect!
