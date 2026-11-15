import unittest
import math
import circle

class TestCircle(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(circle.area(8), math.pi * 8 ** 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(4), 2 * math.pi * 4)

    def test_zero_value_raises(self):
        with self.assertRaises(ValueError):
            circle.area(0)

        with self.assertRaises(ValueError):
            circle.perimeter(0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            circle.area(-4)

        with self.assertRaises(ValueError):
            circle.perimeter(-4)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            circle.area("3")

        with self.assertRaises(TypeError):
            circle.perimeter("3")

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            circle.area(2 - 5j)

        with self.assertRaises(ValueError):
            circle.perimeter(2 - 5j)

    def test_bool_raises(self):
        with self.assertRaises(TypeError):
            circle.area(True)

        with self.assertRaises(TypeError):
            circle.perimeter(True)