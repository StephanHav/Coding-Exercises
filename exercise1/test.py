import unittest
from .exercise1 import find_duplicates

# Define class to test find_duplicates function 
class TestFindDuplicates(unittest.TestCase):

    # Test the example given in the instructions
    def test_given_example(self):
        self.assertEqual(find_duplicates(["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]), ["a", "c", "d"])

    # Test case with no duplicates in input list
    def test_no_duplicates(self):
        self.assertEqual(find_duplicates(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]), [])

    # Test case with only duplicates in input list
    def test_all_duplicates(self):
        self.assertEqual(find_duplicates(["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]), ["a"])

    # Test case with input list containing elements of various data types
    def test_mixed_elements(self):
        self.assertEqual(find_duplicates([b'\x00', 2, 2, "a", "b", 4, b'\x00', "a", "c", 1]), [b'\x00', 2, "a"])

    # Test case witha  single element as input
    def test_single_element(self):
        self.assertEqual(find_duplicates(["a"]), [])

    # Test case with a single element in input list
    def test_empty_list(self):
        self.assertEqual(find_duplicates([]), [])

    # Test case with an input list of 1 million elements
    def test_big_list(self):
        self.assertEqual(find_duplicates(["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]*100000), ["b", "a", "c", "e", "d"])

if __name__ == '__main__':
    unittest.main()
