from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("file:///F:/Training/PeopleNTech/BITM%20Online%2012/12th%20Class/mutiselect.html")

option1 = driver.find_element(By.XPATH, '/html/body/select/option[1]')
option2 = driver.find_element(By.XPATH, '/html/body/select/option[2]')
option3 = driver.find_element(By.XPATH, '/html/body/select/option[3]')

ActionChains(driver).key_down(Keys.CONTROL).click(option1).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(option2).key_up(Keys.CONTROL).perform()