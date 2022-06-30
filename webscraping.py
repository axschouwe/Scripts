
#houses the GET function and will be used to create a connection the website, will return the source code of the website
import requests 
#used for parsing the html
from bs4 import BeautifulSoup 

#website to scrape
url = 'http://quotes.toscrape.com/'
#variable for get request to url
response = requests.get(url)
#parsing text responses using the lxml parser
soup = BeautifulSoup(response.text, 'lxml')

#from analyzing the html we see that all quotes are in the span class=text element
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
#remove the html (span, class = text)
# for quote in quotes:
#     print(quote.text)

#add the author to the quotes and remove the html
for i in range (0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    