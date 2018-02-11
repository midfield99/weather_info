import os
import requests

def get_api_response(city):
    api_key = os.environ.get('OWM_API_KEY')
    base_url = os.environ.get('OWM_BASE_URL')

    if not api_key or not base_url or api_key =='FAKE_KEY':
        err = "Environmental variable retrieval failed. Was the API key set and config file sourced?"
        raise SystemExit(err)

    url = base_url + 'weather?q={}&appid={}'.format(city, api_key)
    return requests.get(url)

bad_response = get_api_response('DesMoines')
good_response = get_api_response('Des Moines')
