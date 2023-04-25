from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/LENOVO/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles/exclude_out_of_stock-exclude_upcoming-stock')
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]' ).click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height:
        break
    old_height=new_height



html = driver.page_source

with open('Smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

