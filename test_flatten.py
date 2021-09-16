import unittest
from exercise import flatten

class TestFlatten(unittest.TestCase):
    def test_string_as_entry(self):
        with self.assertRaises(Exception):
            flatten("bla")

    def test_int_as_entry(self):
        with self.assertRaises(Exception):
            flatten(1)

    def test_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_integers_list(self):
        self.assertEqual(flatten([1,2,3,4,5,6]), [1,2,3,4,5,6])

    def test_nested_list_of_int(self):
        self.assertEqual(flatten([1, [2, 34, 2, 3, [3, [4, 5]]]]), [1,2,34,2,3,3,4,5])

    def test_string_int_list(self):
        with self.assertRaises(Exception):
            flatten([1, "bla"])

    def test_None_int_list(self):
        with self.assertRaises(Exception):
            flatten([1,2,3,4,5,None])

    def test_float_int_list(self):
        with self.assertRaises(Exception):
            flatten([1, [2, 34.85, 2, 3, [3, [4, 50.25]]]])

    def test_a_None_in_nested_list(self):
        with self.assertRaises(Exception):
            flatten([1, [2, 34, 2, 3, [3, [None, 5]]]])


