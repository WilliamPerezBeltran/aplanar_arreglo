import unittest
from exercise import Flatten


class TestFlatten(unittest.TestCase):
    def test_1(self):
        flatten_1 = Flatten()
        flatten_1.set_flatten_list([1, [2, [3, [4, 5]]]])
        self.assertEqual(flatten_1.get_flatten_list(), [1, 2, 3, 4, 5])

    def test_2(self):
        flatten_2 = Flatten()
        flatten_2.set_flatten_list([1, 2, 3, 4])
        self.assertEqual(flatten_2.get_flatten_list(), [1, 2, 3, 4])

    def test_3(self):
        flatten_3 = Flatten()
        flatten_3.set_flatten_list([1, [2, 34, 2, 3, [3, [4, 5]]]])
        self.assertEqual(flatten_3.get_flatten_list(), [1, 2, 34, 2, 3, 3, 4, 5])

    def test_4(self):
        flatten_4 = Flatten()
        flatten_4.set_flatten_list([1, [2, 34, 2, 3, [3, [4, 5]]]])
        self.assertEqual(flatten_4.get_flatten_list(), [1, 2, 34, 2, 3, 3, 4, 5])

    def test_5(self):
        flatten_5 = Flatten()
        flatten_5.set_flatten_list([1, 2])
        self.assertEqual(flatten_5.get_flatten_list(), [1, 2])

    def test_6(self):
        flatten_6 = Flatten()
        flatten_6.set_flatten_list([1, 2, [9, 8, 7, 5]])
        self.assertEqual(flatten_6.get_flatten_list(), [1, 2, 9, 8, 7, 5])

    def test_7(self):
        flatten_7 = Flatten()
        flatten_7.set_flatten_list([])
        self.assertEqual(flatten_7.get_flatten_list(), [])

    def test_8(self):
        flatten_8 = Flatten()
        self.assertEqual(flatten_8.set_flatten_list(23), "Must be a list")

    def test_9(self):
        flatten_9 = Flatten()
        self.assertEqual(flatten_9.set_flatten_list("string"), "Must be a list")

    def test_10(self):
        flatten_10 = Flatten()
        self.assertEqual(flatten_10.set_flatten_list("c"), "Must be a list")
