import requests

from bs4 import BeautifulSoup

act_number = int(input())
link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find_all('h2')[act_number].text)
