![Cronus](/docs/_static/cronus-extended-logo.png?raw=true "Cronus Logo")

Cronus is a collection of utilities to force timing restrictions on computation in Python

## Install

```
pip install cronus
```

or

```
git clone http://github.com/anayjoshi/cronus
python setup.py install
```

## Usage

As of now, Cronus implements two features:

* Allows a continuous while loop to run at a fixed frequency

```python
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
```

* Implements a `@timeout` decorator to forcefully timeout a function call

```python
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
```

## Documentation

The documentation of cronus can be found at http://cronus.readthedocs.org
