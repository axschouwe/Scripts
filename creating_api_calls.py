#create a get query sent to API with parameters (using python's request library)
#API returns JSON response
import requests
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0012993441012'}
response = requests.get(baseUrl, params=parameters)
print(response.url)