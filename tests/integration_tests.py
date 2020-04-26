import unittest
import json
import requests
from index import app
import warnings

# Import test data
with open('tests/test-data/login.json') as json_file:
    login_data = json.load(json_file)
with open('tests/test-data/login_bad_password.json') as json_file:
    login_bad_data = json.load(json_file)
with open('tests/test-data/login_bad_body.json') as json_file:
    login_bad_body = json.load(json_file)

# Set URL where API calls are made
url = "http://localhost:5000"


class E2ETestCase(unittest.TestCase):

    # Remove user first if exists
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        warnings.filterwarnings(
            "ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")

    # Remove Test User
    @classmethod
    def tearDownClass(cls):
        pass

    # Test logging in
    def test_login(self):
        # sending get request and saving the response as response object
        response = self.app.post(url + "/login", data=json.dumps(login_data), headers={
                                 'content-type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    # Test failed log in
    def test_failed_login(self):
        # sending get request and saving the response as response object
        response = self.app.post(url + "/login", data=json.dumps(login_bad_data), headers={
                                 'content-type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    # Test bad body
    def test_failed_login_body(self):
        # sending get request and saving the response as response object
        response = self.app.post(url + "/login", data=json.dumps(login_bad_body), headers={
                                 'content-type': 'application/json'})
        self.assertEqual(response.status_code, 400)

# End of E2ETestCase --------------------------------------------------------------------------------------------------------------------


def suite():  # Need to define a suite as setUp and tearDown are called per test otherwise
    suite = unittest.TestSuite()
    suite.addTest(E2ETestCase('login'))
    suite.addTest(E2ETestCase('test_failed_login'))
    suite.addTest(E2ETestCase('test_failed_login_body'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
