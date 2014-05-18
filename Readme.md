# Cronus

Cronus is the Greek god of time. This package implements an environment aware 'sleep' function. A typical use case of this library is as follows:

If you want to run a particular computation periodically, say every 1 seconds, then traditionally, the structure of the program looks as shown below

```
while True:
    do_some_work()
    time.sleep(1)
```

In the above implementation, if the function `do_some_work()` takes say 0.5 seconds to execute, then the total time spent in one loop is 1.5 seconds. To force the total time spent in the loop to be 1 sec, you might want to modify the sleep to 0.5 seconds

```
while True:
    do_some_work()
    time.sleep(0.5)
```

The user of the program would have to keep track of the time taken by `do_some_work()` to make it run every 1 seconds. Enter *cronus*!

```
while True:
    do_some_work()
    cronus.sleep(1)
```

Cronus would try its best to force the sleep duration in the loop to 1 seconds.
