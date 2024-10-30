import unittest
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.post('/add', data={'a': '2', 'b': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'5.0', response.data)

    def test_subtract(self):
        response = self.app.post('/subtract', data={'a': '5', 'b': '3'})
        self.assertIn(b'2.0', response.data)

    def test_multiply(self):
        response = self.app.post('/multiply', data={'a': '4', 'b': '3'})
        self.assertIn(b'12.0', response.data)

    def test_divide(self):
        response = self.app.post('/divide', data={'a': '10', 'b': '2'})
        self.assertIn(b'5.0', response.data)

    def test_divide_by_zero(self):
        response = self.app.post('/divide', data={'a': '10', 'b': '0'})
        self.assertIn(b'Error: Division by zero', response.data)
        
    def test_modulus(self):
        response = self.app.post('/Modulus', data={'a': '10', 'b': '3'})
        self.assertIn(b'1.0', response.data)

if __name__ == '__main__':
    unittest.main()