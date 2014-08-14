import unittest
from merge_sort import *

class SortingTest(unittest.TestCase):
	def test_merge_sort(self):
		self.assertEqual([0], merge_sort([0]))
		self.assertEqual([-2,-1,0,1,2], merge_sort([-1,-2,2,1,0]))
		
		self.assertEqual(["a"], merge_sort(["a"]))
		self.assertEqual(["a","b","c","d"], merge_sort(["c","d","b","a"]))
		
		self.assertEqual([1,2,3,"a","b","c"], merge_sort(["b","c",2,"a",1,3]))
		
if __name__ == '__main__':
	unittest.main()