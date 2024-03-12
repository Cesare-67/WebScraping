import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
aside = soup.find('aside')
for child in aside.children:
    print(child.name)



