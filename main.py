import os
import requests

def validate_json_response(res):
    code = str(res.get('cod')) #I've seen both number response codes and string response code from this api.
    if code != '200':
        err = "Api call unsuccessful. Code: {} Error Message: {}"
        raise LookupError(err.format(code, res.get("message")))

def get_api_response(city):
    api_key = os.environ.get('OWM_API_KEY')
    base_url = os.environ.get('OWM_BASE_URL')

    if not api_key or not base_url or api_key =='FAKE_KEY':
        err = "Environmental variable retrieval failed. Was the API key set and config file sourced?"
        raise SystemExit(err)

    url = base_url + 'weather?q={}&appid={}'.format(city, api_key)
    response = requests.get(url).json()
    validate_json_response(response)

    return response
