from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

choose_file = driver.find_element(By.NAME, 'upfile')

choose_file.send_keys('F:\Training\PeopleNTech\BITM Online 12\Course Outline.pdf')
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/form/input[3]').click()
