import requests
import re
from bs4 import BeautifulSoup

def search(keyword):

    keyword = keyword.upper()

    response = requests.get('http://example.webscraping.com/')

    html_sem_tags = BeautifulSoup(response.text, 'html.parser')

    text = html_sem_tags

    busca = re.findall(keyword, text.text.upper())

    for i in busca:
        i=i.lower()

    print(busca)


search('google')
search('login')
search('Albania')