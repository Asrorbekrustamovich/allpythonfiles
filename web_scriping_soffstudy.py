import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "https://soffstudy.uz/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="__next")
job_cards = results.find_all("div", class_="card-blog-1 hover-up")
image_urls = []
titles = []
for job_card in job_cards:
    image_container = job_card.find("div", class_="advantage-image")
    image = image_container.find("img") if image_container else None
    title = job_card.find("h4", class_="color-white")
    image_url = image["src"] if image else "No image found"
    title_text = title.text if title else "No title found"
    image_urls.append(image_url)
    titles.append(title_text)

data = {"Title": titles, "Image URL": image_urls}
df = pd.DataFrame(data)
df.to_excel("scraped_data.xlsx", index=False)

print("Data has been written to scraped_data.xlsx")
