from urllib import response
import requests
from bs4 import BeautifulSoup

print('Search on urban dictionary:')
search = input()
response = requests.get(
    'https://www.urbandictionary.com/define.php?term='+search)
soup = BeautifulSoup(response.text, 'html.parser')
definitions = soup.select("div.break-words.meaning")
no = 0
if not definitions:
    print("There are no definitions for this word. ¯\_(ツ)_/¯")
else:
    for no, definition in enumerate(definitions, start=1):
        print(str(no)+". "+definition.get_text())
