import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        app.testing = True
        self.client = app.test_client()

    def test_home_page(self):
        # Send a GET request to the home route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Assert the response status code is 200
        self.assertIn(b"Welcome to Development server!!",
                      response.data)  # Assert the response contains the expected text

    def test_home_post_request(self):
        # Send a POST request to the home route
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)  # Assert the response status code is 200
        self.assertIn(b"Welcome to Development server!!",
                      response.data)  # Assert the response contains the expected text


if __name__ == '__main__':
    unittest.main()
