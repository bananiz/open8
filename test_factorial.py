import unittest
from asd import factorial  # Предполагается, что функция factorial находится в файле factorial_module.py

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1, "Факториал 0 должен быть равен 1")

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1, "Факториал 1 должен быть равен 1")

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120, "Факториал 5 должен быть равен 120")
        self.assertEqual(factorial(3), 6, "Факториал 3 должен быть равен 6")

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800, "Факториал 10 должен быть равен 3628800")

if __name__ == '__main__':
    unittest.main()
