#create a get query sent to API with parameters (using python's request library)
#API returns JSON response

import requests
import json
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
#look up upc of item 
parameters = {'upc': '650240016349'}
response = requests.get(baseUrl, params=parameters)
print(response.url)


content = response.content
#converts json into python dictionary
info = json.loads(content)
# print(type(info))
#print(info)
#specify items directory
item = info['items']
#look at the first element under items
itemInfo = item[0]
#result for title
title = itemInfo['title']
#result for brand
brand = itemInfo['brand']
print(title)
print(brand)
