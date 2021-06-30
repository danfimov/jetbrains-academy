import requests
from bs4 import BeautifulSoup

act_number = int(input())
link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find_all('a')[act_number - 1].get('href'))
