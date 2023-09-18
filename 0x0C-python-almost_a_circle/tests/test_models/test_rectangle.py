#!/usr/bin/python3
"""
Module contain unittest for ``Rectangle`` Class
"""

import unittest
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):
    """
    Test ``Rectangle`` class
    """

    def test_valid_values(self):
        """Test Rectangle with valid values"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(5, 8, 6, 9, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 8)
        self.assertEqual(r3.x, 6)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(6, 7)
        r4.width = 5
        r4.height = 6
        r4.x = 5
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 6)
        self.assertEqual(r4.x, 5)
        self.assertEqual(r4.y, 0)

    def test_invalid_values(self):
        """Test Rectangle with invalid values"""

        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "abc", 5)
        self.assertRaises(TypeError, Rectangle, 11, [1, 2, 3])
        self.assertRaises(TypeError, Rectangle, [1, 2, 4], 11, 1, 1)
        self.assertRaises(TypeError, Rectangle, 8, (9, 0))
        self.assertRaises(TypeError, Rectangle, (9, 0), 11)
        self.assertRaises(TypeError, Rectangle, 8, {1, 2, 3})
        self.assertRaises(TypeError, Rectangle, {1, 2, 3}, 9)
        self.assertRaises(TypeError, Rectangle, 8, (9, 0), 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, (9, 0), 8, 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, 8, {"name": "abc"}, 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, {"name": "abc"}, 8, 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, "abc", 5.7, 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, 8.9, 8, 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, float('inf'), 8, 5, 6, 5)
        self.assertRaises(TypeError, Rectangle, 8, 9, float('nan'), "5", 5)
        self.assertRaises(TypeError, Rectangle, [1, 2], {1, 2}, 10.9, "5")
        self.assertRaises(TypeError, Rectangle, 9, 10, 11, "12")
        self.assertRaises(TypeError, Rectangle, 9, None, 11, 12)

        self.assertRaises(ValueError, Rectangle, 0, 1, 2, 3, 4)
        self.assertRaises(ValueError, Rectangle, 1, 0, 2, 3, 4)
        self.assertRaises(ValueError, Rectangle, -1, 1, 2, 3, 4)
        self.assertRaises(ValueError, Rectangle, 1, -2, 3, 4, 5)
        self.assertRaises(ValueError, Rectangle, -1, 0, 3, 4, 5)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, 4)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4, 5)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, -4)
        self.assertRaises(ValueError, Rectangle, 0, 0, -1, -2)
        self.assertRaises(ValueError, Rectangle, 1, -2, -1, 1)

    def test_mising_width_height(self):
        """Test if missing width or height or both"""

        self.assertRaises(TypeError, Rectangle, 10)
        self.assertRaises(TypeError, Rectangle)

    def test_area(self):
        """Test the ``area`` method of the ``Rectangle`` class"""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        r4 = Rectangle(1, 2)
        self.assertRaises(TypeError, r4.area(), 1)

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout."""

        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display(self):
        """Test the ``display`` method of the ``Rectangle`` class"""

        r1 = Rectangle(1, 2)
        c = TestRectangle.capture_stdout(r1, "display")
        rec_dis = "#\n#\n"
        self.assertEqual(c.getvalue(), rec_dis)

        r2 = Rectangle(2, 2)
        c = TestRectangle.capture_stdout(r2, "display")
        rec_dis = "##\n##\n"
        self.assertEqual(c.getvalue(), rec_dis)

        r3 = Rectangle(2, 2)
        rec_dis = "##\n##\n"
        self.assertRaises(TypeError, r3.display(), 1, 2)

        r4 = Rectangle(2, 3, 2, 2, 3)
        c = TestRectangle.capture_stdout(r4, "display")
        rec_dis = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(c.getvalue(), rec_dis)

        r5 = Rectangle(3, 2, 1, 0)
        c = TestRectangle.capture_stdout(r5, "display")
        rec_dis = " ###\n ###\n"
        self.assertEqual(c.getvalue(), rec_dis)

        r6 = Rectangle(3, 2, 1, 0, 7)
        rec_dis = " ###\n ###\n"
        self.assertRaises(TypeError, r6.display(), 1, 2)

        r7 = Rectangle(4, 3, 2, 1, 7)
        r7.width = 3
        r7.height = 2
        r7.x = 1
        r7.y = 0
        c = TestRectangle.capture_stdout(r7, "display")
        rec_dis = " ###\n ###\n"
        self.assertEqual(c.getvalue(), rec_dis)

    def test_str(self):
        """Test ``__str__`` method"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(c.getvalue(), expected_output)

        r2 = Rectangle(5, 5, 1)
        c = TestRectangle.capture_stdout(r2, "print")
        expected_output = '[Rectangle] ({}) 1/0 - 5/5\n'.format(r2.id)
        self.assertEqual(c.getvalue(), expected_output)

        r3 = Rectangle(6, 7, 9)
        r3.width = 5
        r3.height = 5
        r3.x = 1
        expected_output = '[Rectangle] ({}) 1/0 - 5/5\n'.format(r2.id)
        self.assertEqual(c.getvalue(), expected_output)

    def test_update(self):
        """Test ``update`` method"""

        r1 = Rectangle(10, 10, 10, 10)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] ({}) 10/10 - 10/10\n'.format(r1.id)
        self.assertEqual(c.getvalue(), expected_output)

        r1.update(89)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] (89) 10/10 - 10/10\n'
        self.assertEqual(c.getvalue(), expected_output)

        r1.update(89, 2)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] (89) 10/10 - 2/10\n'
        self.assertEqual(c.getvalue(), expected_output)

        r1.update(89, 2, 3)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] (89) 10/10 - 2/3\n'
        self.assertEqual(c.getvalue(), expected_output)

        r1.update(89, 2, 3, 4)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] (89) 4/10 - 2/3\n'
        self.assertEqual(c.getvalue(), expected_output)

        r1.update(89, 2, 3, 4, 5)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] (89) 4/5 - 2/3\n'
        self.assertEqual(c.getvalue(), expected_output)

        r1.update(89, 2, 3, 4, 5, 6)
        c = TestRectangle.capture_stdout(r1, "print")
        expected_output = '[Rectangle] (89) 4/5 - 2/3\n'
        self.assertEqual(c.getvalue(), expected_output)

        # this is some examples of invalid values and it work with all casess
        self.assertRaises(TypeError, r1.update, 1, "invalid")
        self.assertRaises(ValueError, r1.update, 1, 1, 0)
        self.assertRaises(ValueError, r1.update, 1, -1)
        self.assertRaises(ValueError, r1.update, 1, 1, -1)
        self.assertRaises(ValueError, r1.update, 1, 1, 1, -2)
        self.assertRaises(ValueError, r1.update, 1, 1, 1, 2, -2)

        # update with **kwargs
        r2 = Rectangle(10, 10, 10, 10)
        c = TestRectangle.capture_stdout(r2, "print")
        expected_output = '[Rectangle] ({}) 10/10 - 10/10\n'.format(r2.id)
        self.assertEqual(c.getvalue(), expected_output)

        r2.update(height=1)
        c = TestRectangle.capture_stdout(r2, "print")
        expected_output = '[Rectangle] ({}) 10/10 - 10/1\n'.format(r2.id)
        self.assertEqual(c.getvalue(), expected_output)

        r2.update(width=1, x=2)
        c = TestRectangle.capture_stdout(r2, "print")
        expected_output = '[Rectangle] ({}) 2/10 - 1/1\n'.format(r2.id)
        self.assertEqual(c.getvalue(), expected_output)

        r2.update(y=1, width=2, x=3, id=89)
        c = TestRectangle.capture_stdout(r2, "print")
        expected_output = '[Rectangle] (89) 3/1 - 2/1\n'
        self.assertEqual(c.getvalue(), expected_output)

        r2.update(x=1, height=2, y=3, width=4)
        c = TestRectangle.capture_stdout(r2, "print")
        expected_output = '[Rectangle] (89) 1/3 - 4/2\n'
        self.assertEqual(c.getvalue(), expected_output)

        # Examples for invalid values with **kwargs
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(width=0)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.update(height=-1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2.update(x=-1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2.update(y=-1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(width="invalid")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.update(height="invalid")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(x="invalid")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(y="invalid")


if __name__ == '__main__':
    unittest.main()
