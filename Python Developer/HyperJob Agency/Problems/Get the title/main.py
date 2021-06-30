import requests

from bs4 import BeautifulSoup

user_input = input()
r = requests.get(user_input)
soup = BeautifulSoup(r.content, 'html.parser')
result = soup.find('h1').text
print(result)