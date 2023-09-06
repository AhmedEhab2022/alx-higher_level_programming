#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the ``max_integer`` function"""

    def test_max_int_list(self):
        """Tests the output of the function
        when the argument is a list of integer
        """

        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([90, 100, 0, 1000, 9]), 1000)
        self.assertEqual(max_integer([9999999, 100, 988749, 100]), 9999999)

    def test_max_float_int_list(self):
        """Tests the output of the function
        when the argument is a list of float
        and integers
        """

        self.assertEqual(max_integer([1.9, 1.8, 99999]), 99999)
        self.assertEqual(max_integer([9.9, 8.8, 5.5]), 9.9)
        self.assertEqual(max_integer([8.7, 1, 2, 4]), 8.7)

    def test_max_without_any_args(self):
        """Tests the output of the function
        without any arguments
        """

        self.assertIsNone(max_integer())

    def test_max_mix_type_list(self):
        """Tests the output of the function
        when the list contain mix of types
        """

        self.assertRaises(TypeError, max_integer, ["ahmed", 1, (0, 1)])
        self.assertRaises(TypeError, max_integer, [[0, 1, 2], "smith", (0, 1)])
        self.assertRaises(TypeError, max_integer, ["ahmed", 1.9, {1, 2, 4}])

    def test_string(self):
        """Tests the output of the function
        when the argument is string
        """

        self.assertEqual(max_integer("ahmed"), 'm')

    def test_list_of_strings(self):
        """Tests the output of the function
        when the argument is list of string
        """

        self.assertEqual(max_integer(["ahmed", "ehab", "smith"]), "smith")

    def test_empty_string(self):
        """Tests the output of the function
        when the argument is empty string
        """

        self.assertIsNone(max_integer(""))

    def test_max_other_types(self):
        """Tests the output of the function
        when the argument is not a list
        """

        self.assertRaises(TypeError, max_integer, 1.9)
        self.assertRaises(TypeError, max_integer, 0)
        self.assertEqual(max_integer((1, 2)), 2)
        self.assertRaises(TypeError, max_integer, {1, 5, 0})


if __name__ == "__main__":
    unittest.main()
