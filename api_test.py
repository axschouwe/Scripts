import urllib
import json
from urllib.parse import urlencode, urlparse
import requests
#first part of api request string before the "?"
baseUrl = 'https://us.rest.logs.insight.rapid7.com/query/'

#api key and search location
parameters = {'x-api-key' : '947a31d3-334d-44ba-a529-500b65cc8c85'}
response = requests.get(baseUrl, params = parameters)
print(response.url)

content = response.content
print(content)