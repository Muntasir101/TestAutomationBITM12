from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path="F:\Training\PeopleNTech\BITM Online 12\TestAutomationBITM12\BrowserDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
