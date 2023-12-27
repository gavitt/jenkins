# test_app.py

import unittest
from app import app  # Import the Flask application from app.py


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data is what we expect
        self.assertEqual(response.data.decode('utf-8'), 'Привет, мир!')


if __name__ == '__main__':
    unittest.main()
