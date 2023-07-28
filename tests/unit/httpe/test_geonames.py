import unittest  
from unittest.mock import patch  
import requests  
from httpe.geonames import call_geonames  

class TestCallGeonames(unittest.TestCase):
    # Test case for a successful API response with two cities.
    def test_call_geonames_success(self):
        mock_response = {'results': [{'name': 'City1'}, {'name': 'City2'}]}
        with patch('httpe.geonames.requests.get', return_value=MockResponse(200, mock_response)):
            result = call_geonames('City')
            # Assert that the response contains the expected city names.
            self.assertEqual(result['geonames'][0]['name'], 'City1')
            self.assertEqual(result['geonames'][1]['name'], 'City2')

    # Test case for handling an API failure (HTTP status code 404).
    def test_call_geonames_failure(self):
        with patch('httpe.geonames.requests.get', return_value=MockResponse(404, {})):
            # Assert that calling call_geonames with 'City' raises a requests.HTTPError.
            with self.assertRaises(requests.HTTPError):
                call_geonames('City')

    # Test case for handling an empty response from the API.
    def test_call_geonames_empty_response(self):
        mock_response = {'geonames': []}
        with patch('httpe.geonames.requests.get', return_value=MockResponse(200, mock_response)):
            result = call_geonames('City')
            # Assert that the response contains an empty list of geonames.
            self.assertEqual(result['geonames'], [])

    def test_call_geonames_no_geonames_key(self):
        mock_response = {'some_other_key': [{'name': 'City1'}, {'name': 'City2'}]}
        with patch('httpe.geonames.requests.get', return_value=MockResponse(200, mock_response)):
            result = call_geonames('City')
            # Assert that the response does not contain the 'geonames' key.
            self.assertNotIn('geonames', result)

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

if __name__ == '__main__':
    unittest.main()
