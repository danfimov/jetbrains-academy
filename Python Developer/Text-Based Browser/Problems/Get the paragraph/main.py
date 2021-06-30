import requests

from bs4 import BeautifulSoup

word = input()
link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')

list_p = soup.find_all('p')
for p in list_p:
    if p.text.find(word) != -1:
        print(p.text)
        break
