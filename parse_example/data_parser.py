from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://befree.ru/zhenskaya/odezhda').text
soup = LxmlSoup(html)

links = soup.find_all('a', class_='sc-4a450f6d-0')

for i, link in enumerate(links):
    url = link.get("href")
    name = link.text()
    price = soup.find_all("div", class_="sc-7b424381-0 fzBzDT")[i].text()
    print(i)
    print(f"Url - {url}")
    print(f"Name - {name}")
    print(f"Price - {price}\n")

