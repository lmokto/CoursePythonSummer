import unittest


def add(a, b):
    return a+b


def mult(a, b):
    return a*b


class TestCalculatorBySum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(1, 4))
        self.assertEqual(7, add(1, 6))
        self.assertEqual(8, add(1, 7))

    def test_add_fail(self):
        self.assertNotEqual(7, add(1, 4))


class TestCalculatorByMult(unittest.TestCase):
    def test_mult(self):
        result = mult(3, 5)
        self.assertEqual(15, result)


class TestingStringMethod(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        self.assertEqual(result, 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(), ['Hello', 'World'])


if __name__ == "__main__":
    unittest.main()

