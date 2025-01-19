import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, -1), -1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(-5, 1), -5)

    def test_division(self):
        # with self.assertRaises(ZeroDivisionError):
        #     self.calc.divide(5, 0)
        self.assertEqual(self.calc.divide(5,0), None)
        self.assertEqual(self.calc.divide(4, 2), 2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,0), 5)
        self.assertEqual(self.calc.subtract(5,2), 3)
