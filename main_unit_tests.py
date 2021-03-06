import io
import json
import sys
import unittest

from unittest.mock import patch
import main

#I don't really like depending on external apis for unit tests,
# so I copied text from response.text to use for api responses.
GOOD_RESPONSE = '{"coord":{"lon":-93.6,"lat":41.59},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"base":"stations","main":{"temp":266.05,"pressure":1020,"humidity":57,"temp_min":265.15,"temp_max":267.15},"visibility":16093,"wind":{"speed":5.1,"deg":250},"clouds":{"all":20},"dt":1518380100,"sys":{"type":1,"id":865,"message":0.0039,"country":"US","sunrise":1518354822,"sunset":1518392646},"id":4853828,"name":"Des Moines","cod":200}'
INVALID_API_KEY_RESPONSE = '{"cod":401, "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}'
INVALID_CITY_RESPONSE = '{"cod":"404","message":"city not found"}'

#This class is for mocking when a function uses requests.get()
# so that tests don't need to actually hit an endpoint.
class requests_mock:
    def json():
        return json.loads(GOOD_RESPONSE)

class TestMain(unittest.TestCase):
    def test_json_response_200(self):
        jsn = json.loads(GOOD_RESPONSE)
        main.validate_json_response(jsn)

    def test_json_response_401(self):
        jsn = json.loads(INVALID_API_KEY_RESPONSE)
        err = "Api call unsuccessful. Code: 401 Error Message: Invalid API key. "
        err += "Please see http://openweathermap.org/faq#error401 for more info."

        self.assertRaisesRegex(LookupError, err, main.validate_json_response, jsn)

    def test_json_response_404(self):
        jsn = json.loads(INVALID_CITY_RESPONSE)
        err = "Api call unsuccessful. Code: 404 Error Message: city not found"
        self.assertRaisesRegex(LookupError, err, main.validate_json_response, jsn)

    def test_response_missing_temp(self):
        jsn = json.loads('{"cod":200}')
        err = "Temperature was not found in response."
        self.assertRaisesRegex(LookupError, err, main.validate_json_response, jsn)

    @patch('main.os.environ.get')
    def test_config_error_api_key_missing(self, envs):
        envs.side_effect = [None, 'Valid_Base_Url']
        err = "Environmental variable retrieval failed. "
        err +="Was the API key set and config file sourced?"
        self.assertRaisesRegex(SystemExit, err, main.get_api_response, "Ames")

    @patch('main.os.environ.get')
    def test_config_error_api_key_default(self, envs):
        envs.side_effect = ['FAKE_KEY', 'Valid_Base_Url']
        err = "Environmental variable retrieval failed. "
        err +="Was the API key set and config file sourced?"
        self.assertRaisesRegex(SystemExit, err, main.get_api_response, "Ames")

    @patch('main.os.environ.get')
    def test_config_error_base_url_missing(self, envs):
        envs.side_effect = ['Valid_Key', None]
        err = "Environmental variable retrieval failed. "
        err +="Was the API key set and config file sourced?"
        self.assertRaisesRegex(SystemExit, err, main.get_api_response, "Ames")


    def test_validate_bad_input(self):
        bad = '!@#$%^&*()_+=`~[]:";<>,.12345667890'
        err = "City is invalid. Only letters, spaces, and '-' are allowed."

        for b in bad:
            self.assertRaisesRegex(ValueError, err, main.validate_input, 'city' + b)

    @patch('main.requests.get')
    @patch('main.input')
    @patch('main.os.environ.get')
    def test_retrieve_temp(self, envs, inp, requests_get):
        envs.side_effect = ['Valid_Key', 'Valid_Base_Url']
        inp.return_value = 'Valid Input'
        output = "The temperature is 266.05 \u00b0F.\n"
        requests_get.side_effect = [requests_mock]

        std_out = io.StringIO()
        sys.stdout = std_out
        main.retrieve_temp()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, std_out.getvalue())

if __name__ == '__main__':
    unittest.main()
