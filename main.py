from bs4 import BeautifulSoup
import requests

url = 'https://www.omgtu.ru/l/?SHOWALL_1=1'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
titles = soup.findAll('h3', class_='news-card__title')
file = open('titles.txt', 'w', encoding='utf-8')
for title in titles:
    file.write(titles[titles.index(title)].text.strip('\n').strip() + '\n')
file.close()
