from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

keyword = 'macbook pro 2015'
main_link = 'https://www.tokopedia.com'
url = 'https://www.tokopedia.com/search?navsource=home&page=25&q={}&srp_component_id=02.01.00.00&st=product'.format(keyword)

path = ".\chromedriver.exe"

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('disable-notifications')
options.add_argument('--disable-infobars')
driver = webdriver.Chrome(chrome_options=options,executable_path=path)

driver.get(url)
i = 1
while i < 1500 :  
  print(i)
  driver.execute_script(f"window.scrollBy(0,{i})","")
  i+=1
wait = WebDriverWait(driver, 1500)
stores = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//html')))
soup = BeautifulSoup(stores[0].get_attribute('innerHTML'),"html.parser")
product = soup.find_all("div",class_="css-1b6t4dn")
print(product)
print(len(product))
# driver.quit()