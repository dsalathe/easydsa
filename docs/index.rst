Welcome to SimpleDSA's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Introduction <self>
   api/index
   examples/index

SimpleDSA is a Python library that provides simple and intuitive implementations of common data structures and algorithms.

Quick Start
----------

Installation
~~~~~~~~~~~

.. code-block:: bash

   pip install simpledsa

Basic Usage
~~~~~~~~~~

.. code-block:: python

   from simpledsa import PriorityQueue

   # Create a min-heap priority queue
   pq = PriorityQueue()

   # Add some items
   pq.push(3)
   pq.push(1)
   pq.push(4)

   # Process items in priority order
   while pq:
       print(pq.pop())  # Prints: 1, 3, 4

Features
--------

- Simple and intuitive API
- Flexible priority queue implementation
- Support for custom priority functions
- Batch operations
- Context manager support
- Comprehensive documentation
- 100% test coverage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
