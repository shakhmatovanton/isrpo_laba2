import unittest
import rectangle


class TestRectangle(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(4.6, 2.3), 4.6 * 2.3)

    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle.perimeter(4.6, 2.3), (4.6 + 2.3) * 2)

    def test_zero_value_raises(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, 0)

        with self.assertRaises(ValueError):
            rectangle.perimeter(0, 0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, -4)

        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, -4)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            rectangle.area(2 - 2j, 7 + 1j)

        with self.assertRaises(ValueError):
            rectangle.perimeter(2 - 2j, 7 + 1j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            rectangle.area("4.6", "2.3")

        with self.assertRaises(TypeError):
            rectangle.perimeter("4.6", "2.3")

    def test_bool_raises(self):
        with self.assertRaises(TypeError):
            rectangle.area(False, False)

        with self.assertRaises(TypeError):
            rectangle.perimeter(True, False)