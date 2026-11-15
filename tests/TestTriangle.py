import unittest
import itertools
import triangle

class TestTriangle(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(2.9, 8.0), 2.9 * 8.0 / 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimeter(2.9, 12.7, 4.4), 2.9 + 12.7 + 4.4)

    def test_perimeter_order_independent(self):
        sides = (6, 8, 10)
        for switched_sides in itertools.permutations(sides):
            self.assertEqual(triangle.perimeter(*sides), triangle.perimeter(*switched_sides))

    def test_perimeter_inequality_raises(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(2, 3, 10)

    def test_zero_value_raises(self):
        with self.assertRaises(ValueError):
            triangle.area(2, 0)

        with self.assertRaises(ValueError):
            triangle.area(0, 2)

        with self.assertRaises(ValueError):
            triangle.perimeter(0, 0, 0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            triangle.area(-3, -5)

        with self.assertRaises(ValueError):
            triangle.perimeter(-2, -6, -7)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            triangle.area(2 + 5j, 3 - 1j)

        with self.assertRaises(ValueError):
            triangle.perimeter(-2 + 8j, 5 + 2j, 3 - 3j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            triangle.area("7.5", "2.4")

        with self.assertRaises(TypeError):
            triangle.perimeter("6", "7", "8")

    def test_bool_raises(self):
        with self.assertRaises(TypeError):
            triangle.area(True, False)

        with self.assertRaises(TypeError):
            triangle.perimeter(False, True, True)