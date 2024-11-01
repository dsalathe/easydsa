API Reference
============

Priority Queue
-------------

.. automodule:: simpledsa.priority_queue
   :members:
   :undoc-members:
   :show-inheritance:

Priority Functions
----------------

.. automodule:: simpledsa.priority_functions
   :members:
   :undoc-members:
   :show-inheritance:

# File: docs/examples.rst
Examples
========

Here are some examples of how to use SimpleDSA:

Priority Queue
-------------

Basic Usage
~~~~~~~~~~

.. code-block:: python

    from simpledsa import PriorityQueue

    # Create a min-heap
    pq = PriorityQueue()

    # Add items
    pq.push(3)
    pq.push(1)
    pq.push(4)

    # Get items in priority order
    while pq:
        print(pq.pop())  # prints: 1, 3, 4
