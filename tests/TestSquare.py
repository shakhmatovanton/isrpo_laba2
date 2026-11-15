import unittest
import square


class TestSquare(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(square.area(6.5), 6.5 ** 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(6.5), 6.5 * 4)

    def test_zero_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(0)

        with self.assertRaises(ValueError):
            square.perimeter(0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(-3)

        with self.assertRaises(ValueError):
            square.perimeter(-3)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(2 + 5j)

        with self.assertRaises(ValueError):
            square.perimeter(2 + 5j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            square.area("6.5")

        with self.assertRaises(TypeError):
            square.perimeter("6.5")

    def test_bool_raises(self):
        with self.assertRaises(TypeError):
            square.area(False)

        with self.assertRaises(TypeError):
            square.perimeter(True)