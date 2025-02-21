import unittest
from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius

class TestConversorTemperatura(unittest.TestCase):
    def test_celsius_para_fahrenheit(self):
        self.assertAlmostEqual(celsius_para_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_para_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_para_fahrenheit(-40), -40)

    def test_fahrenheit_para_celsius(self):
        self.assertAlmostEqual(fahrenheit_para_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_para_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_para_celsius(-40), -40)

if __name__ == "__main__":
    unittest.main()
