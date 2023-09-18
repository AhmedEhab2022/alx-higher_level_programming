#!/usr/bin/python3
"""
Module contain unittest for ``Rectangle`` Class
"""

import unittest
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """
    Test ``Square`` class
    """

    @staticmethod
    def capture_stdout(squr, method):
        """Captures and returns text printed to stdout."""

        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(squr)
        else:
            squr.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_size_str_display(self):
        """Test ``size``and ``area``, ``__str__``and ``display`` methods"""

        s1 = Square(5)
        c = TestSquare.capture_stdout(s1, "print")
        expected = "[Square] ({}) 0/0 - 5\n".format(s1.id)
        self.assertEqual(c.getvalue(), expected)
        self.assertEqual(s1.area(), 25)
        c = TestSquare.capture_stdout(s1, "display")
        expected = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(c.getvalue(), expected)

        s2 = Square(2, 2)
        c = TestSquare.capture_stdout(s2, "print")
        expected = '[Square] ({}) 2/0 - 2\n'.format(s2.id)
        self.assertEqual(c.getvalue(), expected)
        self.assertEqual(s2.area(), 4)
        c = TestSquare.capture_stdout(s2, "display")
        expected = "  ##\n  ##\n"
        self.assertEqual(c.getvalue(), expected)

        s3 = Square(3, 1, 3)
        c = TestSquare.capture_stdout(s3, "print")
        expected = '[Square] ({}) 1/3 - 3\n'.format(s3.id)
        self.assertEqual(c.getvalue(), expected)
        self.assertEqual(s3.area(), 9)
        c = TestSquare.capture_stdout(s3, "display")
        expected = '\n\n\n ###\n ###\n ###\n'
        self.assertEqual(c.getvalue(), expected)
