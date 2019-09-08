import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://adityesh.github.io/Adityesh/')

soup = BeautifulSoup(response.text,'html.parser')
projects = soup.findAll(class_= "project-container")

with open('project.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title','Project-Name']
    csv_writer.writerow(headers)


    for project in projects:
        title = project.findAll(class_="right-container")
        column_1 = "Project Title"
        for project_title in title:
            project_heading = project_title.find('span').get_text()
            print("Project Title : " +project_heading + "\n")
            csv_writer.writerow([column_1,project_heading])
    