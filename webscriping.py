import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_cards = results.find_all("div", class_="card-content")
for job_card in job_cards:
     title_element = job_card.find("h2", class_="title")
     company_element = job_card.find("h3", class_="company")
     location_element = job_card.find("p", class_="location")
     time=job_card.find('time')
     print(title_element.text)
     print(company_element.text)
     print(location_element.text)
     print(time.text)
     print()

