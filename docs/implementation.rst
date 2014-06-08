Cronus Implementation
=====================

Implementation withing cronus is divided into two modules: `beat` and `timeout`


beat
----

The `beat` module implements the fixed frequency feature

.. autofunction:: beat.set_rate


.. autofunction:: beat.true


.. autofunction:: beat.sleep


.. autoclass:: beat.BeatError

timeout
-------

The `timeout` module implements, obviously, the timeout feature

.. autofunction:: timeout.timeout

.. autoclass:: timeout.TimeoutError
