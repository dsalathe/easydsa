import unittest
from easydsa import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
    
    def test_empty_queue(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEqual(len(self.pq), 0)
    
    def test_push_pop(self):
        # Add your test cases here
        pass