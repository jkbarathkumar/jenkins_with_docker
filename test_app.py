import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True  

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)  # Check for Hello, World! content

    def test_404(self):
        response = self.client.get('/non-existent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
