from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://befree.ru/zhenskaya').text
soup = LxmlSoup(html)

links = soup.find_all('a', class_='sc-4a450f6d-0')
for link in links:
    url = link.get("href")

for i, link in enumerate(links):
    url = "https://befree.ru/zhenskaya" + link.get("href") # получаем ссылку товара
    name = link.text()  # извлекаем наименование из блока со ссылкой
    price = soup.find_all("div", class_="sc-7b424381-0 fzBzDT")[i].text()  # извлекаем цену

    print(i)
    print(f"Url - {url}")
    print(f"Name - {name}")
    print(f"Price - {price}\n")

