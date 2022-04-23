from ast import keyword
from cgitb import html
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

keyword = 'macbook pro 2015'
main_link = 'https://www.tokopedia.com'
url = 'https://www.tokopedia.com/search?st=product&q={}&srp_component_id=02.01.00.00&navsource=home'.format(keyword)

path = ".\chromedriver.exe"

chrome = Options()
chrome.add_argument('--no-sandbox')
chrome.add_argument('disable-notifications')
chrome.add_argument('--disable-infobars')

driver = webdriver.Chrome(executable_path=path,options=chrome)
driver.set_window_position(-10000,0)
driver.get(url)

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html,"html.parser")

product = soup.find_all("div",class_="css-1b6t4dn")
driver.quit()
print(product[0].get_text())
