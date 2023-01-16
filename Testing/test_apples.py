from Apples import Fruit
import unittest

class TestFruit(unittest.TestCase):
    def test_get_apple(self):
        my_fruit = Fruit()
        
        # Assert that the return value of the get_apple() method is "apple"
        self.assertEqual("apple", my_fruit.get_apple())
