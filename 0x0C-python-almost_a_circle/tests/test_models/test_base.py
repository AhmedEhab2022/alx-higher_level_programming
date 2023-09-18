#!/usr/bin/python3
"""
Unittest for Class ``Base``
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests the ``Base`` Class"""

    def test_no_args(self):
        """
        Tests the public instance attribute ``id``
        when make an instance from it without passing any args
        """

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_args(self):
        """
        Tests the public instance attribute ``id``
        when make an instance from it with args
        """

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base(50)
        self.assertEqual(b5.id, 50)

    def test_no_and_with_args(self):
        """
        Tests the public instance attribute ``id``
        when make an instance from it with args and without args
        """

        b6 = Base(10)
        self.assertEqual(b6.id, 10)

        b7 = Base()
        b8 = Base()
        self.assertEqual(b7.id, b8.id - 1)

        b9 = Base(5)
        self.assertEqual(b9.id, 5)

        b10 = Base()
        self.assertEqual(b10.id, b8.id + 1)

    def test_public_id(self):
        """
        Tests the public instance attribute ``id``
        when the user assign it to an integer Value
        """

        b1 = Base()
        b1.id = 12
        self.assertEqual(b1.id, 12)

        b2 = Base(12)
        b2.id = 80
        self.assertEqual(b2.id, 80)

    def test_id_with_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)


if __name__ == "__main__":
    unittest.main()
