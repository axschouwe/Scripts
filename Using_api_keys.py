#https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
#https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
import requests
#first part of api request string before the "?"
baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
#api key and search location
parameters = {'APPID' : 'a794f6b81dc4ba6a884a92ad5a7487bd', 'q':'Denver,US'}
response = requests.get(baseUrl, params = parameters)
print(response.content)