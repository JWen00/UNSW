import requests 
from bs4 import BeautifulSoup
import re

r = requests.get('https://en.wikipedia.org/wiki/Hacker')
# print(r.text)    # Server's response 
# print(r.content) # Website body (HTML)  asd

soup = BeautifulSoup(r.content, features='html.parser') 
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print (link.get('href'))