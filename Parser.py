from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

URL = 'https://ru.investing.com/currencies/usd-rub'
options = Options()  # Создание опций для открытого браузер
options.add_argument('-headless')  # Добавление опции, чтоб браузер открывался в фоновом режиме
driver = webdriver.Firefox(options=options)
def parse():
    driver.get(URL)
    element = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span")
    ruble = (BeautifulSoup(element.text, "html.parser"))
    ruble1 = float((ruble.text).replace(',','.'))
    return ruble1
