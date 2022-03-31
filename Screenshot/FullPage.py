from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://apple.com")
time.sleep(5)

driver.save_full_page_screenshot("F:\Training\PeopleNTech\BITM Online 12\TestAutomationBITM12\ScreenshotFiles\FullpageApple.png")

driver.close()