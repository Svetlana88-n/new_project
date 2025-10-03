from LxmlSoup import LxmlSoup
import requests
import re

html = requests.get('https://befree.ru/zhenskaya/odezhda').text
soup = LxmlSoup(html)

links = soup.find_all('a', class_='sc-4a450f6d-0')

for i, link in enumerate(links):
    url = link.get("href")
    full_text = link.text()
    name = full_text

    price_match = re.search(r'(\d+₽)', full_text)
    if price_match:
        price = price_match.group(1)
        name = re.sub(r'\d+₽', '', full_text).strip()

    print(i)
    print(f"Url - {url}")
    print(f"Name - {name}")
    print(f"Price - {price}\n")

