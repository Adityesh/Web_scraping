import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://adityesh.github.io/Adityesh/')

soup = BeautifulSoup(response.text,'html.parser')
projects = soup.findAll(class_= "project-container")

for project in projects:
    title = project.findAll(class_="right-container")
    for project_title in title:
        print(">>>" + project_title.find('span').get_text())
        print("----------------")
    