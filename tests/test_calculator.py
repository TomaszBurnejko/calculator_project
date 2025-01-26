import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_addition(self):
        self.assertEqual(self.calculator.calculate("2+3"), 5)
    def test_subtraction(self):
        self.assertEqual(self.calculator.calculate("5-2"), 3)
    def test_multiplication(self):
        self.assertEqual(self.calculator.calculate("3*4"), 12)
    def test_division(self):
        self.assertEqual(self.calculator.calculate("10/2"), 5)
    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate("2+")

if __name__ == '__main__':
unittest.main()