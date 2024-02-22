import unittest
from unittest.mock import patch
from project import rate_parser, convert

class TestProjectFunctions(unittest.TestCase):

    def test_rate_parser(self):
        # Test rate_parser with a mock response
        # Replace the expected_result with an appropriate value
        expected_result = 1.234  # Replace with the expected result
        mock_response = """
            <p class="result__BigRate-sc-1bsijpp-1 dPdXSB">1.234 EUR</p>
        """
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.text = mock_response
            result = rate_parser("USD", "EUR")
        self.assertEqual(result, expected_result)

    def test_convert(self):
        # Test convert with a mock response from rate_parser
        # Replace the expected_result with an appropriate value
        expected_result = 123.4  # Replace with the expected result
        mock_rate_parser = unittest.mock.Mock(return_value=1.234)
        with patch('project.rate_parser', mock_rate_parser):
            result = convert("USD", "EUR", 100)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
