Cronus Implementation
=====================

Implementation withing cronus is divided into two sub-packages: `beat` and `timeout`


beat
----

The `beat` package implements the fixed frequency feature

.. autofunction:: beat.set_rate


.. autofunction:: beat.true


.. autofunction:: beat.sleep


.. autoclass:: beat.BeatError

timeout
-------

The `timeout` package implements, obviously, the timeout feature

.. autofunction:: timeout.timeout

.. autoclass:: timeout.TimeoutError
