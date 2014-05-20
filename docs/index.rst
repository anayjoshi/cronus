.. Cronus documentation master file, created by
   sphinx-quickstart on Sun May 18 12:39:54 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cronus's documentation!
=======================

Contents:

.. toctree::
   :maxdepth: 2

   tutorial
   cronus

Cronus is a useful little library for performing certain computation at a fixed frequency, by being agnostic to the time taken by the computation.

.. code-block:: console

    pip install cronus

Cronus implements a dynamic *sleep()* function to ensure a fixed loop frequency

.. code-block:: python

    cronus.set_rate(2) # 2 Hz
    while cronus.true():
        # do some time consuming work here
        cronus.sleep() # total loop duration would be 0.5 sec

as opposed to

.. code-block:: python

    while True:
        # do some time consuming work here
        time.sleep()
