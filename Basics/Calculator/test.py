import unittest
import calculator


class TestCalculatorBySum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, calculator.add(1, 4))


if __name__ == "__main__":
    unittest.main()


