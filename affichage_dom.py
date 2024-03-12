import requests
from bs4 import BeautifulSoup

# Fonction pour parcourir récursivement l'arbre DOM
def traverse_dom(element, level=0):
    # afficher l'élément actuel
    if element.name:
        print(f"{' ' * level}<{element.name}>")

    # Si l'élément a des enfants, les parcourir aussi
    if hasattr(element, "children"):
        for child in element.children:
            traverse_dom(child, level + 1)

# Commencer le parcours depuis la racine de l'arbre
traverse_dom(soup)
