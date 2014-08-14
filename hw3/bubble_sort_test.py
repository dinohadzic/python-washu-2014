import unittest
from bubble_sort import *

class SortingTest(unittest.TestCase):
	def test_bubble_sort(self):
		self.assertEqual([0], bubble_sort([0]))
		self.assertEqual([-2,-1,0,1,2], bubble_sort([-1,-2,2,1,0]))
		
		self.assertEqual(["a"], bubble_sort(["a"]))
		self.assertEqual(["a","b","c","d"], bubble_sort(["c","d","b","a"]))
		
		self.assertEqual([1,2,3,"a","b","c"], bubble_sort(["b","c",2,"a",1,3]))
		
if __name__ == '__main__':
	unittest.main()