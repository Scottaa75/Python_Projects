from bs4 import BeautifulSoup
import requests


url = 'https://www.yahoo.com'


def find_hyperlink(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        lookup = link.get('href')
        print(lookup)
    print('<End of links ==========================Hyperlinks=============================== End of Links>')
    print()


def find_js_link(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.find_all('script'):
        lookup = link.get('src')
        if lookup:
            print(lookup)
    print('<End of links ==========================JavaScript=============================== End of Links>')
    print()


find_js_link(url)
find_hyperlink(url)
