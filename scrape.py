import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://adityesh.github.io/Adityesh/')

soup = BeautifulSoup(response.text,'html.parser')

print(soup)