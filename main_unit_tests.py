#I don't really like depending on apis for unit tests,
# so I copied text from response.text to use for api responses.
GOOD_RESPONSE='{"coord":{"lon":-93.6,"lat":41.59},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"base":"stations","main":{"temp":266.05,"pressure":1020,"humidity":57,"temp_min":265.15,"temp_max":267.15},"visibility":16093,"wind":{"speed":5.1,"deg":250},"clouds":{"all":20},"dt":1518380100,"sys":{"type":1,"id":865,"message":0.0039,"country":"US","sunrise":1518354822,"sunset":1518392646},"id":4853828,"name":"Des Moines","cod":200}'
INVALID_CITY_RESPONSE='{"cod":"404","message":"city not found"}'
INVALID_API_KEY_RESPONSE='{"cod":401, "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}'
