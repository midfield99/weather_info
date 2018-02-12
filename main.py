import os
import requests

def validate_json_response(res):
    #I've seen both number response codes and string response code from this api.
    code = str(res.get('cod'))
    if code != '200':
        err = "Api call unsuccessful. Code: {} Error Message: {}"
        raise LookupError(err.format(code, res.get("message")))
    elif res.get('main', {}).get('temp') is None:
        raise LookupError("Temperature was not found in response.")

#Rate limiting should definitely be looked at if this was going to be used.
# But I wouldn't expect excessive API usage with a simple command prompt program.
def get_api_response(city):
    api_key = os.environ.get('OWM_API_KEY')
    base_url = os.environ.get('OWM_BASE_URL')

    if not api_key or not base_url or api_key =='FAKE_KEY':
        err = "Environmental variable retrieval failed. Was the API key set and config file sourced?"
        raise SystemExit(err)

    url = base_url + 'weather?q={}&appid={}&units=imperial'.format(city, api_key)
    response = requests.get(url).json()

    validate_json_response(response)

    return response


#Note, this validation approach isn't entirely accurate.
# It should allow nearly all cities,
# but I have found some cities with special characters.
# But this method is simple.
#
# I also checked a couple cities with abbreviations (like Ft. Worth)
# and it looks like the api returns 404s with some common abbreviations.
# So I'm ok not accepting abbreviations or periods.
#
# I'm also not implementing spell check.
def validate_input(city):
    place = city.replace(' ','').replace('-','')
    if not place.isalpha():
        msg = "City is invalid. Only letters, spaces, and '-' are allowed."
        raise ValueError(msg)

#Note, the state is intentionally ignored.
# I've checked the API documentation and it doesn't look like there is an endpoint for a city/state pair.
# Just city/country. This will cause issues, for instance a lot of states have a city Riverside.
#
# I've also checked temps on the site via the search bar, multiple results can be returned,
# but again it looks like adding a state does not change ordering. Riverside,Iowa and Riverside,California
# both returned the same results in the same order.
# It looks like the api endpoint just returns the first item in that list.
# 
# using a zip code to retrieve temperatures would probably be much more accurate.
def retrieve_temp():
    city = input("What city are you in?\n")
    validate_input(city)
    res = get_api_response(city)
    temp = res.get('main', {}).get('temp')

    print("The temperature is {} \u00b0F.".format(temp))

if __name__ == '__main__':
    retrieve_temp()
