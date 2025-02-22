import unittest
from app import app

class TestConversorAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_celsius_para_fahrenheit(self):
        response = self.app.get('/celsius-para-fahrenheit?celsius=25')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fahrenheit', response.json)

    def test_fahrenheit_para_celsius(self):
        response = self.app.get('/fahrenheit-para-celsius?fahrenheit=77')
        self.assertEqual(response.status_code, 200)
        self.assertIn('celsius', response.json)

    def test_invalid_celsius(self):
        response = self.app.get('/celsius-para-fahrenheit?celsius=abc')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_invalid_fahrenheit(self):
        response = self.app.get('/fahrenheit-para-celsius?fahrenheit=xyz')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
