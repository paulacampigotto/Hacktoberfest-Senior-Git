import unittest
from Triangle import *
from Square import *
from Circle import *


class TestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(Triangle(3, 5).area(), 7.5)

    def test_square_area(self):
        self.assertEqual(Square(3, 5).area(), 15)

    def test_circle_area(self):
        self.assertEqual(Circle(3).area(), 28.274333882308138)

    def test_circle_volume(self):
        self.assertEqual(Circle(3).volume(), 113.09733552923255)


if __name__ == "__main__":
    unittest.main()


# python3 -m unittest
