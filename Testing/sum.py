class MathOperations:
    def sum_list(self, lst):
        if lst is None:
            return 0
        return sum(lst)

import unittest

class TestMathOperations(unittest.TestCase):
    def test_sum_list_with_elements(self):
        # Instantiate an object of the MathOperations class
        math_ops = MathOperations()
        
        lst = [1, 2, 3, 4]
        
        # Assert that the return value of the sum_list() method is 10
        self.assertEqual(10, math_ops.sum_list(lst))
        
    def test_sum_list_with_empty_list(self):
        math_ops = MathOperations()
        lst = []
        self.assertEqual(0, math_ops.sum_list(lst))
        
    def test_sum_list_with_one_element(self):
        math_ops = MathOperations()
        lst = [5]
        self.assertEqual(5, math_ops.sum_list(lst))
        
    def test_sum_list_with_multiple_elements(self):
        math_ops = MathOperations()
        lst = [1,2,3,4,5]
        self.assertEqual(15, math_ops.sum_list(lst))
        
    def test_sum_list_with_none(self):
        math_ops = MathOperations()
        self.assertEqual(0, math_ops.sum_list(None))
