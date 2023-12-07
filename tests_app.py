from unittest import TestCase
from app import app

class TestApp(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_result_route(self):
        data = {
            'convert-from': 'USD',
            'convert-to': 'EUR',
            'amount': '100'
        }
        response = self.app.post('/result', data=data, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'\xe2\x82\xac', response.data)  