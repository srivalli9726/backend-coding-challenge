import unittest  
from unittest.mock import patch  
import requests  
from impl.suggestions import get_suggestions, get_score  
from httpe.geonames import call_geonames  

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

class TestGetScore(unittest.TestCase):
    # Test case for get_score function with high population.
    def test_get_score_with_high_population(self):
        geoname = {'population': 1000000}
        score = get_score(geoname)
        self.assertEqual(score, 1.0)

    # Test case for get_score function with low population.
    def test_get_score_with_low_population(self):
        geoname = {'population': 1000}
        score = get_score(geoname)
        self.assertEqual(score, 0.9)

    # Test case for get_score function with zero population.
    def test_get_score_with_zero_population(self):
        geoname = {'population': 0}
        score = get_score(geoname)
        self.assertEqual(score, 0.8)

class TestGetSuggestions(unittest.TestCase):
    # Test case for get_suggestions function with no results.
    def test_get_suggestions_with_no_results(self):
        suggestions = get_suggestions('New York')
        self.assertListEqual(suggestions['suggestions'], [])

    # Test case for get_suggestions function with one result.
    def test_get_suggestions_with_one_result(self):
        with patch.object(requests, 'get', return_value=MockResponse(200, {'results': [{'name': 'New York City'}]})) as mock_get:
            suggestions = get_suggestions('New York')
            self.assertListEqual(suggestions['suggestions'], [{'name': 'New York City'}])
            mock_get.assert_called_with('http://api.geonames.org/searchJSON?q=New+York&country=CA,US&fcode=ppl')

    # Test case for get_suggestions function with multiple results.
    def test_get_suggestions_with_multiple_results(self):
        with patch.object(requests, 'get', return_value=MockResponse(200, {'results': [{'name': 'New York City'}, {'name': 'Los Angeles'}]})) as mock_get:
            suggestions = get_suggestions('New')
            self.assertListEqual(suggestions['suggestions'], [{'name': 'New York City'}, {'name': 'Los Angeles'}])
            mock_get.assert_called_with('http://api.geonames.org/searchJSON?q=New&country=CA,US&fcode=ppl')

