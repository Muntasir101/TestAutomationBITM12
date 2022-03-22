from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://demo.opencart.com/")

# my_account = driver.find_element_by_link_text("My Account")
my_account = driver.find_element(By.LINK_TEXT, 'My Account')
my_account.click()
# login = driver.find_element_by_link_text('Login')
login = driver.find_element(By.LINK_TEXT, 'Login')
login.click()