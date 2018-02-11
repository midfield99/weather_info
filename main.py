import requests

API_KEY = FAKE_KEY
#api.openweathermap.org/data/2.5/weather?q={city name}
BASE_URL='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

good_response_text='{"coord":{"lon":-93.6,"lat":41.59},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"base":"stations","main":{"temp":266.05,"pressure":1020,"humidity":57,"temp_min":265.15,"temp_max":267.15},"visibility":16093,"wind":{"speed":5.1,"deg":250},"clouds":{"all":20},"dt":1518380100,"sys":{"type":1,"id":865,"message":0.0039,"country":"US","sunrise":1518354822,"sunset":1518392646},"id":4853828,"name":"Des Moines","cod":200}'
bad_response_text='{"cod":"404","message":"city not found"}'

bad_response = requests.get(BASE_URL.format('DesMoines', API_KEY))
good_response = requests.get(BASE_URL.format('Des Moines', API_KEY))
