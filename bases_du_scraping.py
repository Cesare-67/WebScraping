# Les bases du scraping

import requests
from bs4 import BeautifulSoup

# Récupérer le contenu d'une page avec requests
response = requests.get("https://www.google.com")
print(response) # retourne <Response [200]
print(response.status_code) # retourne 200
response.raise_for_status() # permet de lever les erreurs si il y en a
print(response.text) # retourne le contenu de la page html
# Sauvegarder le contenu
with open("index.html", "w") as f:
    f.write(response.text)

# Analyse du contenu avec BeautifulSoup
url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser") # création de la variable qui récupère le contenu
print(soup.prettify()) # permet afficher html de manière lisible



